#!/usr/bin/env python3
"""Run one Japanese request with a local Kev checkpoint."""

import argparse
import json

from kev.api import SystemOneRequest, to_answers, to_record
from kev.checkpoint import Checkpoint, LoadOptions


REQUEST = {
    "state": "請求が二重になっているため、利用者が至急の確認を求めている。",
    "questions": {
        "department": {
            "type": "choice",
            "instructions": "担当部署を選んでください。",
            "criteria": {
                "billing": "請求、決済、返金",
                "technical": "技術的な問題",
                "general": "一般的な問い合わせ",
            },
        },
        "urgent": {
            "type": "noul",
            "instructions": "優先対応が必要ですか？",
        },
        "priority": {
            "type": "score",
            "instructions": "対応優先度を評価してください。",
            "criteria": ["低", "中", "高"],
        },
    },
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--device", choices=("mps", "cuda", "cpu"), default="mps")
    parser.add_argument("--backend", choices=("auto", "torch", "mlx"), default="auto")
    args = parser.parse_args()

    request = SystemOneRequest.model_validate(REQUEST)
    record, metadata = to_record(request)
    tokenizer, model = Checkpoint(args.model).load(
        args.device,
        LoadOptions(backend=args.backend),
    )
    encoded = model.encode(tokenizer, record)
    probabilities = [values.tolist() for values in model.probs(encoded)]
    result = {
        "model": "kev-0.8b-japanese-instruct",
        "answers": to_answers(probabilities, metadata),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
