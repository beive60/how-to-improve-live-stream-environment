# EP013 / VT-05: NVIDIA Broadcast GPU負荷ベンチマーク - AI処理の実測コスト

## 必要な動画素材

### 画面キャプチャ

- NVIDIA Broadcastの設定画面（ノイズキャンセリング / 背景除去 / オートフレームの各機能トグル）
- タスクマネージャーのパフォーマンスタブ（GPU使用率・GPUメモリ）
- GPU-Zのセンサータブ（GPU Load, Memory Used, Temperature 等の時系列表示）
- OBSのエンコーダー設定画面（NVENC設定）
- OBS統計パネル（レンダリングラグ / エンコードラグ表示）

### デモ映像

- ベースライン計測: ゲームのみ起動時のGPU負荷・FPS表示
- ゲーム + OBS（録画/配信）起動時のGPU負荷・FPS表示
- ゲーム + OBS + NVIDIA Broadcast（ノイズキャンセリングのみ）起動時の計測
- ゲーム + OBS + NVIDIA Broadcast（背景除去のみ）起動時の計測
- ゲーム + OBS + NVIDIA Broadcast（全機能ON）起動時の計測
- 各条件でのゲームプレイ映像（FPSカウンター表示付き）
- 負荷が高い状態での配信映像品質の劣化デモ（フレームドロップ等）

### 図解・テロップ素材

- テスト条件一覧表（GPU型番 / ゲームタイトル / 設定 / 解像度）
- ベンチマーク結果の棒グラフ（各条件でのGPU使用率・FPS・フレームドロップ率）
- GPU世代別の対応状況一覧表（RTX 20xx / 30xx / 40xx）
- AI処理のリソースコストと代替手段の比較表（NVIDIA Broadcast vs VSTノイズキャンセリング vs ハードウェア対策）

## 必要機材

### 所有済み

- PC2: NVIDIA GeForce RTX 3060（NVIDIA Broadcast対応、NVENC対応、VRAM 12GB）
- PC1: AMD Radeon RX 7900 XT（NVIDIA Broadcast非対応。比較対象として「NVIDIA非搭載環境での代替策」解説に活用可能）

### 追加購入

なし。本エピソードはPC2のRTX 3060で全デモを実施可能。GPU-Z、タスクマネージャー等の計測ツールは無料。
