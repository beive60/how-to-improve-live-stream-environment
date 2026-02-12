# proj_how-to-be-VTuber

VTuber配信環境構築に特化した技術情報チャンネルの企画・制作管理リポジトリ

## ディレクトリ構成

```
.
├── planning/          戦略・企画ドキュメント
├── production/        動画制作（台本・素材・編集メモ）
├── scripts/           運用自動化スクリプト
└── README.md          本ファイル
```

### planning/

チャンネル戦略と動画企画の管理ドキュメントを格納する。

| ファイル | 内容 |
| --- | --- |
| overview.md | チャンネル戦略指針書（ビジョン、ターゲット、差別化戦略、実行計画） |
| channel-growth-strategy.md | チャンネル成長戦略（YouTubeアルゴリズム最適化、クロスプラットフォーム導線、パーソナルブランド構築、IP資産活用） |
| content-catalog.md | コンテンツカタログ（動画企画の一覧、所属ドメイン、Phase、ステータス） |
| dependency-map.md | 依存関係マップ（コンテンツ間の前提知識関係、推奨視聴順序） |
| priority-matrix.md | 優先度マトリクス（検索需要 x 制作難易度 x 差別化効果 x アルゴリズム適合性の評価） |

### production/

動画単位のサブディレクトリで制作物を管理する。

```
production/
├── EP001-obs-audio-desync/
│   ├── script.md          台本
│   ├── notes.md           編集メモ・検証記録
│   └── assets/            サムネイル素材・図版等
├── EP002-.../
```

命名規則: `EP{連番3桁}-{トピック概要}`

### scripts/

配信運用やチャンネル管理の自動化スクリプトを格納する。
