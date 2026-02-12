# EP024 / DO-02: OBS WebSocket入門 - 外部プログラムからのOBS制御基礎

## 必要な動画素材

### 画面キャプチャ

- OBSのWebSocket設定画面（ツール > WebSocketサーバー設定: ポート番号、認証設定）
- WebSocketクライアントツール（Websocat / Insomnia / ブラウザDevTools等）の画面
- Pythonスクリプトエディタ（VS Code等）でのobs-websocket-pyコード表示
- OBS WebSocket APIドキュメントのWebページ（主要なリクエスト/イベントの一覧）
- 接続テスト成功時のログ画面

### デモ映像

- OBS WebSocketサーバーを有効化し、認証パスワードを設定する手順デモ
- WebSocketクライアントツールでOBSに接続し、手動でリクエストを送信するデモ
- GetSceneList リクエストでシーン一覧を取得するデモ
- SetCurrentProgramScene リクエストでシーンを切り替えるデモ
- SetInputMute リクエストで音声ミュートを切り替えるデモ
- Python（obs-websocket-py）で簡単な制御スクリプトを実行するデモ
- イベントのサブスクリプション（SceneChanged等）を受信するデモ

### 図解・テロップ素材

- OBS WebSocketのアーキテクチャ図（OBS ←WebSocket→ クライアント の通信構造）
- 主要リクエスト/レスポンスの一覧表（シーン操作 / ソース操作 / 音声操作 / 配信制御）
- 主要イベントの一覧表（状態変化の通知）
- WebSocket v5 プロトコルの認証フロー図

## 必要機材

### 所有済み

- PC2（OBS + Python実行環境）

### 追加購入

なし。本エピソードはソフトウェア完結（OBS WebSocketプラグイン、Python, obs-websocket-py, VS Code）。
