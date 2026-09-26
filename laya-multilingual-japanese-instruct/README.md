---
license: apache-2.0
base_model: convaiinnovations/laya-multilingual
library_name: laya-mlx
tags:
  - japanese
  - decision-model
  - mlx
---

# Laya Multilingual Japanese Instruct

[`convaiinnovations/laya-multilingual`](https://huggingface.co/convaiinnovations/laya-multilingual) をベースに、日本語の指示に対する判断能力を強化したファインチューニングモデルです。

このリポジトリでは Apple Silicon Mac 向けの MLX checkpoint を配布します。

## Setup

Python 3.11〜3.13 と [uv](https://docs.astral.sh/uv/) を使用します。

```bash
cd laya-multilingual-japanese-instruct
uv sync
```

## Run

```bash
uv run python examples/predict.py --model ./model-mlx
```

JSONファイルを指定して実行する場合:

```bash
uv run laya-mlx predict \
  --model ./model-mlx \
  --state-file examples/state.json \
  --questions examples/questions.json
```

Pythonからは次のように読み込みます。

```python
import laya_mlx

model = laya_mlx.load("./model-mlx", dtype="float16", batch_size=16)
result = model.predict(state, questions)
```

質問形式は `choice`、`noul`、`score` に対応します。具体的なJSON形式は [`examples/questions.json`](./examples/questions.json) を参照してください。

## Notes

- 通常の最大入力長は1,024 tokenです。
- 出力確率やconfidenceは正解を保証しません。
- calibration warningが表示された質問形式のconfidenceは、未校正として扱ってください。

## License

Apache License 2.0。元モデルと関連プロジェクトの帰属は [`../THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md) を参照してください。本モデルは Laya または Convai Innovations の公式モデルではありません。
