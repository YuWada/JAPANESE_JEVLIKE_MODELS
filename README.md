# JAPANESE_JEVLIKE_MODELS

日本語の指示に対する判断能力を強化した、Jev-like decision model の公開リポジトリです。

| モデル | ベースとなる公開モデル | 実行方法 |
| --- | --- | --- |
| [Kev-0.8B Japanese Instruct](./kev-0.8b-japanese-instruct/) | [`jaredpalmer/kev-0.8b`](https://huggingface.co/jaredpalmer/kev-0.8b) | Kev / PyTorch・MLX |
| [Laya Multilingual Japanese Instruct](./laya-multilingual-japanese-instruct/) | [`convaiinnovations/laya-multilingual`](https://huggingface.co/convaiinnovations/laya-multilingual) | `laya-mlx` / Apple Silicon |

各モデルのインストール方法とサンプルコードは、それぞれのディレクトリにあります。

## License

このリポジトリの派生モデルと文書は [Apache License 2.0](./LICENSE) で公開します。元モデルと下層モデルのライセンス・帰属は [THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md) に記載しています。

本モデルは元プロジェクトの公式配布物ではありません。
