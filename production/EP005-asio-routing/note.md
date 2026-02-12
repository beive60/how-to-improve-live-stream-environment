# EP005 / AE-05: ASIO Routing実践 - FL Studio ASIO/ASIO Link Proで低遅延ルーティングを実現する

## 必要な動画素材

### 画面キャプチャ

- FL Studio ASIOドライバの設定画面（バッファサイズ・入出力割り当て）
- ASIO Link Proの仮想ルーティングマトリクス画面
- VoiceMeeter Bananaのルーティング画面（比較用）
- Windowsサウンド設定画面（既定のデバイス選択）
- DAWmon等のレイテンシー計測ツール画面
- オーディオインターフェースのASIO設定画面

### デモ映像

- Windowsオーディオエンジン（WASAPI）経由時のレイテンシー計測デモ
- ASIO経由時のレイテンシー計測デモ（差を定量表示）
- FL Studio ASIOで複数アプリケーションに音声をルーティングする操作デモ
- ASIO Link Proで仮想ケーブルを作成・接続する操作デモ
- VoiceMeeterとのレイテンシー比較デモ
- ルーティング変更がリアルタイムで反映される様子

### 図解・テロップ素材

- Windowsオーディオスタック図（アプリ → WASAPI → カーネルミキサー → ドライバ vs アプリ → ASIO → ドライバ）
- ASIO / WASAPI / WDM の特性比較表（レイテンシー、排他制御、マルチクライアント）
- ルーティング構成図（マイク入力 → ASIO → OBS / Discord / ゲーム の並列出力）
- レイテンシー実測結果の比較棒グラフ

## 必要機材

### 所有済み

- マイク: Audio-Technica AT-2020

### 追加購入（必須）

- DSP内蔵オーディオIF（RME Babyface Pro FS / MOTU M4 / Audient iD14 mk II）
  - 本エピソードの主題はASIOドライバによる低遅延ルーティング。Roland VT-4のASIO対応は限定的でマルチクライアント検証に不向き
  - ASIO設定画面（バッファサイズ・入出力割り当て）のデモに本格的なオーディオIFが必要
  - AE-06, AE-07, AE-08 でも継続使用するため、本エピソード制作前までに確保すること
