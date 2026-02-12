# EP028 / DO-06: YouTube API + Python自動化 - コメント分析と運用効率化

## 必要な動画素材

### 画面キャプチャ

- Google Cloud ConsoleのAPIライブラリ画面（YouTube Data API v3 の有効化）
- Google Cloud Consoleの認証情報画面（OAuth 2.0クライアントID / APIキーの作成）
- VS Codeでのpythonスクリプトコード表示（YouTube APIクライアント初期化）
- pip install コマンドのターミナル実行画面（google-api-python-client等のインストール）
- Jupyter Notebook等でのデータ分析結果表示画面

### デモ映像

- Google Cloud ConsoleでAPIを有効化し、認証情報を取得する手順デモ
- Pythonスクリプトで動画のコメント一覧を取得するデモ（API呼び出し → JSON結果表示）
- 取得したコメントデータをpandasでDataFrame化し、集計・フィルタリングするデモ
- センチメント分析（感情分析）の実行デモ（ポジティブ/ネガティブの分類結果表示）
- 分析結果をmatplotlib / seabornでグラフ化するデモ
- 配信メタデータ（タイトル、説明文、タグ）の自動更新スクリプト実行デモ
- cron / タスクスケジューラでの定期実行設定デモ

### 図解・テロップ素材

- YouTube Data API v3 のアーキテクチャ図（アプリ → OAuth認証 → API → YouTubeデータ）
- APIクォータ制限の解説表（各エンドポイントのコスト単位と日次上限）
- 自動化ワークフロー図（データ取得 → 分析 → レポート生成 → 通知 の流れ）
- 主要エンドポイント一覧表（CommentThreads / Videos / LiveChatMessages 等）

## 必要機材

### 所有済み

- PC2（Python実行環境。CUDA対応 GPUがあればセンチメント分析の高速化も可能）

### 追加購入

なし。本エピソードはソフトウェア完結（Python, google-api-python-client, Google Cloud Console）。YouTube Data API v3の無料枚数内で全デモ実施可能。
