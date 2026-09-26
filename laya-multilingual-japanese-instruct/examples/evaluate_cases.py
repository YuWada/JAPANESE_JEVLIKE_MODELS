#!/usr/bin/env python3
"""Run a simple labelled JSON case file against a Laya MLX checkpoint."""

import argparse
import json
from pathlib import Path
from typing import Any

import laya_mlx


def predicted_value(answer: dict[str, Any], question_type: str) -> Any:
    if question_type == "choice":
        return answer["choice"]
    if question_type == "noul":
        return answer["noul"] >= 0.5
    if question_type == "score":
        probabilities = answer["probabilities"]
        return int(max(probabilities, key=probabilities.get))
    raise ValueError(f"Unsupported question type: {question_type}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--cases", required=True, type=Path)
    parser.add_argument(
        "--dtype",
        choices=("float16", "float32", "bfloat16"),
        default="float16",
    )
    args = parser.parse_args()

    cases = json.loads(args.cases.read_text(encoding="utf-8"))
    if not isinstance(cases, list):
        raise ValueError("The cases file must contain a JSON array")

    agent = laya_mlx.load(args.model, dtype=args.dtype, batch_size=16)
    correct = 0

    for index, case in enumerate(cases, 1):
        question_id = str(case.get("id", f"case-{index}"))
        question = dict(case["question"])
        result = agent.predict(case["state"], {question_id: question})
        answer = result["answers"][question_id]
        predicted = predicted_value(answer, question["type"])
        expected = case["expected"]
        matched = predicted == expected
        correct += int(matched)
        print(
            json.dumps(
                {
                    "id": question_id,
                    "predicted": predicted,
                    "expected": expected,
                    "correct": matched,
                    "answer": answer,
                },
                ensure_ascii=False,
            )
        )

    total = len(cases)
    accuracy = correct / total if total else 0.0
    print(f"Result: {correct}/{total} ({accuracy:.1%})")


if __name__ == "__main__":
    main()
