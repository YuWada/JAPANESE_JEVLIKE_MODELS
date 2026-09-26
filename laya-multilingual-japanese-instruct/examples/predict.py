#!/usr/bin/env python3
"""Run a small Japanese typed-decision example with a Laya MLX checkpoint."""

import argparse
import json

import laya_mlx


STATE = "ユーザーは請求が二重になっていると連絡している。至急の確認を希望している。"

QUESTIONS = {
    "department": {
        "type": "choice",
        "instructions": "どの担当部署へ振り分けるべきですか？",
        "criteria": {
            "billing": "請求、決済、返金に関する問題",
            "technical": "技術的な不具合",
            "general": "一般的な問い合わせ",
        },
    },
    "urgent": {
        "type": "noul",
        "instructions": "この問い合わせは緊急対応が必要ですか？",
        "criteria": {
            "false": "通常の順番で対応できる",
            "true": "優先して人間が確認する必要がある",
        },
    },
    "priority": {
        "type": "score",
        "instructions": "対応優先度を評価してください。",
        "criteria": ["低", "中", "高"],
    },
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model",
        required=True,
        help="Local MLX checkpoint directory or Hugging Face model ID",
    )
    parser.add_argument(
        "--dtype",
        choices=("float16", "float32", "bfloat16"),
        default="float16",
    )
    args = parser.parse_args()

    agent = laya_mlx.load(args.model, dtype=args.dtype, batch_size=16)
    result = agent.predict(STATE, QUESTIONS)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
