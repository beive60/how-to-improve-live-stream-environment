# EP004 / AE-04: LUFS音圧最適化 - YouTubeの-14 LUFS基準に合わせる方法

## 必要な動画素材

### 画面キャプチャ

- VSTラウドネスメーター（Youlean Loudness Meter Free 等）のプラグインUI画面
- OBSでのVSTプラグイン設定画面（ラウドネスメーターの挿入位置）
- OBSゲインフィルタ / コンプレッサーフィルタの調整画面
- YouTube Studioのアップロード済み動画の音量表示画面（Stats for Nerds）

### デモ映像

- LUFS未調整の状態でのラウドネスメーター表示（-14 LUFSから外れている様子）
- ゲインとコンプレッサーで段階的に-14 LUFSへ近づけていく調整過程
- 調整完了後のラウドネスメーター表示（-14 LUFS付近で安定している様子）
- YouTubeにアップロードした動画のラウドネス正規化前後の音量差デモ
- 音圧が高すぎる場合にYouTubeが自動で下げる挙動のデモ

### 図解・テロップ素材

- LUFS / LKFS / dBFS の違いを示す対照表
- YouTubeラウドネス正規化の処理フロー図（アップロード → 解析 → 正規化）
- Integrated LUFS / Short-term LUFS / Momentary LUFS の計測区間を示す図
- 各配信プラットフォームの推奨ラウドネスターゲット比較表（YouTube / Twitch / Podcast）

## 必要機材

### 所有済み

- マイク: Audio-Technica AT-2020
- オーディオIF: Roland VT-4

### 追加購入

なし。本エピソードはソフトウェア完結（Youlean Loudness Meter Free + OBSゲイン/コンプレッサーフィルタ）。
