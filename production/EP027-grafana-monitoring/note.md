# EP027 / DO-05: 配信システムモニタリング - Grafana + InfluxDBによるリソース可視化

## 必要な動画素材

### 画面キャプチャ

- Grafanaダッシュボードの完成画面（CPU / GPU / ネットワーク / OBS統計のパネル群）
- Grafanaのパネル編集画面（クエリ設定・可視化オプション）
- InfluxDBの管理画面（バケット / データエクスプローラー）
- Telegraf等のデータ収集エージェントの設定ファイル画面
- Grafanaのアラート設定画面（閾値ベースのアラートルール作成）
- Docker Desktop画面（コンテナ一覧: Grafana / InfluxDB / Telegraf）

### デモ映像

- Docker ComposeでGrafana + InfluxDB + Telegrafを一括起動する手順デモ
- Telegrafの設定ファイルを編集し、CPU/GPU/ネットワークメトリクスの収集を有効化する操作デモ
- OBS WebSocket経由でOBS統計（フレームドロップ、エンコード時間等）を収集するスクリプトの実行デモ
- Grafanaでダッシュボードを一からパネルを追加して構築する操作デモ
- 配信中のリアルタイムリソースモニタリング画面（負荷がグラフに反映される様子）
- アラート発火デモ（CPU使用率が閾値を超えた際の通知）
- 配信後の事後分析デモ（パフォーマンス低下が発生した時間帯をグラフから特定）

### 図解・テロップ素材

- モニタリングスタックの構成図（PC → Telegraf → InfluxDB → Grafana → ダッシュボード/アラート）
- 収集すべきメトリクス一覧表（CPU / GPU / RAM / Network / Disk / OBS固有指標）
- Docker Compose構成ファイルの構造図
- ダッシュボードレイアウトの設計図（パネル配置の推奨例）

## 必要機材

### 所有済み

- PC2（Docker, Grafana, InfluxDB, Telegraf動作用。RTX 3060搭載でGPUメトリクス収集も可能）

### 追加購入

なし。本エピソードはソフトウェアスタック完結（Docker + Grafana + InfluxDB + Telegraf、全て無料/OSS）。
