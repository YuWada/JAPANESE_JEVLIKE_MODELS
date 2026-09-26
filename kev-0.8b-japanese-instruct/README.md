---
license: apache-2.0
base_model:
  - jaredpalmer/kev-0.8b
  - Qwen/Qwen3.5-0.8B-Base
library_name: kev
tags:
  - japanese
  - decision-model
  - lora
---

# Kev-0.8B Japanese Instruct

[`jaredpalmer/kev-0.8b`](https://huggingface.co/jaredpalmer/kev-0.8b) をベースに、日本語の指示に対する判断能力を強化したファインチューニングモデルです。

このディレクトリで配布するのは LoRA adapter と pointer head です。実行時に [`Qwen/Qwen3.5-0.8B-Base`](https://huggingface.co/Qwen/Qwen3.5-0.8B-Base) が自動的に取得されます。

## Setup

Python 3.12 または 3.13 と [uv](https://docs.astral.sh/uv/) を使用します。

```bash
cd kev-0.8b-japanese-instruct
uv sync
```

## Run

Apple Silicon Mac:

```bash
uv run python examples/predict.py --model ./model --device mps
```

NVIDIA GPU:

```bash
uv run python examples/predict.py --model ./model --device cuda --backend torch
```

CPU:

```bash
uv run python examples/predict.py --model ./model --device cpu --backend torch
```

初回実行時はベースモデルを Hugging Face から取得します。

## Server

TypeSafe System One互換のローカルAPIとして起動できます。

```bash
uv run python -m kev.serve --run ./model --port 8009
```

```bash
curl -s http://127.0.0.1:8009/v1/systemone \
  -H 'content-type: application/json' \
  --data @examples/request.json
```

## License

Apache License 2.0。元モデルと関連プロジェクトの帰属は [`../THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md) を参照してください。本モデルは Kev、Qwen、TypeSafe の公式モデルではありません。
