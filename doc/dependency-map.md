# Dependency Map

<!--
このファイルは、コンテンツカタログ（content-catalog.md）の各動画間の
前提知識関係を定義し、推奨視聴順序とプレイリスト構成を明確にするものです。

依存関係の読み方:
  「A → B」は「Aを視聴してからBを視聴することを推奨」の意味です。
  Aの内容を前提知識としてBが成り立つ関係を示します。

  「必須」: Bを理解するためにAの視聴がほぼ必須
  「推奨」: Aを見ていなくても理解できるが、見ていると理解が深まる

各動画のIDはコンテンツカタログ（content-catalog.md）を参照してください。
-->

## 1. ドメイン内依存関係

### AE: オーディオエンジニアリング

<!--
オーディオドメインは依存関係が最も複雑。
AE-01（音ズレ解決）が全体の起点になっている。
音ズレを解決する過程でサンプリングレートやバッファサイズの概念を学ぶため、
他のオーディオコンテンツの基礎知識となる。
-->

```
AE-01 音ズレ根治
  │
  ├──[推奨]──→ AE-02 VST処理チェーン
  │               │
  │               ├──[必須]──→ AE-03 ノイズゲート最適化
  │               │
  │               ├──[必須]──→ AE-04 LUFS音圧最適化
  │               │
  │               ├──[推奨]──→ AE-07 Audio Ducking
  │               │
  │               └──[必須]──→ AE-09 スタンドアロンVSTホスト
  │                               │
  │                               └──[推奨]──→ AE-05 ASIO Routing
  │
  └──[推奨]──→ AE-05 ASIO Routing
                  │
                  └──[必須]──→ AE-06 Hardware Loopback
                                 │
                                 └──[推奨]──→ AE-08 Dante / AoIP
```

```yaml
- id: AE-01
  required: なし
  recommended: なし
  note: エントリーポイント。音ズレは最も検索される問題

- id: AE-02
  required: なし
  recommended: AE-01
  note: VSTの概念を初めて導入。AE-01で学ぶ音声基礎があると理解しやすい

- id: AE-03
  required: AE-02
  recommended: なし
  note: ノイズゲートはVSTプラグインの一種。AE-02のチェーン概念が必要

- id: AE-04
  required: AE-02
  recommended: なし
  note: LUFS計測にはVSTメータープラグインを使用するため、AE-02が前提

- id: AE-05
  required: なし
  recommended: AE-01
  note: ASIO自体は独立したトピックだが、AE-01のバッファ概念の理解が有効

- id: AE-06
  required: AE-05
  recommended: なし
  note: ハードウェアルーティングはASIOの上位概念。ASIO理解が前提

- id: AE-07
  required: AE-02
  recommended: なし
  note: サイドチェインコンプはVSTプラグインで実装するため、AE-02が必要

- id: AE-08
  required: AE-06
  recommended: なし
  note: ハードウェアルーティングの理解なしにDante導入は困難

- id: AE-09
  required: AE-02
  recommended: なし
  note: >
    AE-02のVSTプラグイン概念が前提。OBS VST2ホストの制約を踏まえた上で、
    スタンドアロンVSTホストによるシステムワイド音声処理へ移行する。
    Discord/コラボ配信が主たるユースケース。
    AE-05（ASIO Routing）への自然な導線も提供する
```

### VT: ビジュアル・トラッキングパイプライン

<!--
VTドメインは比較的シンプルな依存関係。
VT-01 と VT-02 が独立したエントリーポイントになっている。
-->

```
VT-01 VTube Studioスムージング     VT-02 OBS色空間/LUT
  │                                   │
  └──[推奨]──→ VT-03 ARKit vs Webcam  └──[推奨]──→ VT-05 NVIDIA Broadcast
                 │
                 └──[必須]──→ VT-04 Blend Shapes
```

```yaml
- id: VT-01
  required: なし
  recommended: なし
  note: エントリーポイント。VTube Studio使用者の共通課題

- id: VT-02
  required: なし
  recommended: なし
  note: エントリーポイント。色空間は独立したトピック

- id: VT-03
  required: なし
  recommended: VT-01
  note: トラッキング手法の比較。VT-01で基本概念に触れていると理解しやすい

- id: VT-04
  required: VT-03
  recommended: なし
  note: ARKitのBlend Shapesを扱うため、ARKit自体の理解（VT-03）が前提

- id: VT-05
  required: なし
  recommended: VT-02
  note: GPU負荷の話題。VT-02のOBS映像パイプライン理解があると有効
```

### NE: ネットワークエンジニアリング

```
NE-01 配信停止の切り分け
  │
  ├──[推奨]──→ NE-02 CBRビットレート設計
  │               │
  │               └──[推奨]──→ NE-06 プラットフォーム再エンコード
  │
  ├──[推奨]──→ NE-03 Ingest Server最適化
  │
  └──[推奨]──→ NE-04 QoS設定
                  │
                  └──[推奨]──→ NE-05 WANボンディング

NE-06 プラットフォーム再エンコード ←── 独立エントリーポイントとしても機能
```

```yaml
- id: NE-01
  required: なし
  recommended: なし
  note: エントリーポイント。診断フローチャートを提供する基礎動画

- id: NE-02
  required: なし
  recommended: NE-01
  note: CBR設計は独立して理解可能だが、NE-01の診断視点があると実践的

- id: NE-03
  required: なし
  recommended: NE-01
  note: Traceroute分析はNE-01の診断フローの延長

- id: NE-04
  required: なし
  recommended: NE-01
  note: QoSはネットワーク基礎の理解が必要。NE-01がその導入になる

- id: NE-05
  required: NE-04
  recommended: なし
  note: ボンディングはQoSの理解（ネットワーク層の知識）が前提

- id: NE-06
  required: なし
  recommended: NE-02
  note: >
    エントリーポイントとしても機能する。NE-02のCBRビットレート設計を
    理解していると、ビットレート効率（bits-per-pixel）の概念がより深く理解できる。
    unknown unknowns型のコンテンツであり、NE-01やNE-02とは異なる検索経路
    （「画質が悪い」「ブロックノイズ」）から流入する視聴者を想定
```

### CM: 構成管理と冗長化設計

```
CM-01 OBS Git管理
  │
  └──[推奨]──→ CM-02 OBSポータブルモード

CM-03 2PC配信構成 ←──[推奨]── AE-05, NE-01（クロスドメイン）
  │
  ├──[推奨]──→ CM-04 回線冗長化
  │
  └──[必須]──→ CM-05 2PC間ファイル同期
                  │
                  └──[推奨]── CM-01 OBS Git管理（クロスドメイン）
```

```yaml
- id: CM-01
  required: なし
  recommended: なし
  note: エントリーポイント。Gitの基本知識があれば視聴可能

- id: CM-02
  required: なし
  recommended: CM-01
  note: プロファイル管理の発展形。CM-01の知識があると移行がスムーズ

- id: CM-03
  required: なし
  recommended: AE-05, NE-01
  note: 2PC構成にはオーディオルーティングとネットワークの基礎が必要

- id: CM-04
  required: なし
  recommended: CM-03, NE-05
  note: 回線冗長化は2PC構成やWANボンディングの知識と組み合わせると実用的

- id: CM-05
  required: CM-03
  recommended: CM-01
  note: >
    2PC構成を前提とするため、CM-03が必須。CM-01のGit管理と対象ファイルが
    一部重なるが、バイナリ素材・継続的双方向同期という異なる問題領域を扱う。
    unknown unknownsに属するため検索流入は限定的。CM-03のEnd Screen経由での
    セッション内誘導を主要な流入経路として設計する
```

### DO: DevOps for Streamers

```
DO-01 Stream Deck/Touch Portal    DO-02 OBS WebSocket入門
                                    │
                                    ├──[必須]──→ DO-04 Streamer.bot自動化
                                    │
                                    └──[推奨]──→ DO-05 Grafana監視

DO-03 VRAM最適化 ←──[推奨]── VT-05（クロスドメイン）

DO-06 YouTube API ←── 独立（プログラミング基礎を前提とする）
```

```yaml
- id: DO-01
  required: なし
  recommended: なし
  note: ハードウェアマクロは独立して学習可能

- id: DO-02
  required: なし
  recommended: なし
  note: WebSocket API入門として独立。ただしOBSの基本操作は前提

- id: DO-03
  required: なし
  recommended: VT-05
  note: GPU負荷の文脈でVT-05と関連するが、独立して理解可能

- id: DO-04
  required: DO-02
  recommended: なし
  note: OBS WebSocket APIの知識なしにStreamer.bot連携は困難

- id: DO-05
  required: なし
  recommended: DO-02
  note: モニタリング自体は独立だが、WebSocketからのデータ収集で連携可能

- id: DO-06
  required: なし
  recommended: なし
  note: Python+APIの独立トピック。プログラミング基礎知識を前提とする
```

## 2. クロスドメイン依存関係

<!--
クロスドメイン依存とは、異なるドメインの動画同士が関連するケースです。
「オーディオの知識がないとネットワーク設定が活かせない」等の関係を示します。
これらは全て「推奨」レベルであり、必須ではありません。
-->

```yaml
- from: AE-05 ASIO Routing
  to: CM-03 2PC配信構成
  relation: 2PC構成ではPC間のオーディオルーティング知識が必要

- from: AE-06 Hardware Loopback
  to: CM-03 2PC配信構成
  relation: ハードウェアルーティングは2PC構成での安定性向上に直結

- from: NE-01 配信停止の切り分け
  to: CM-03 2PC配信構成
  relation: 2PC間のネットワーク診断にNE-01の手法が必要

- from: NE-04 QoS
  to: CM-04 回線冗長化
  relation: QoS設定は冗長化設計と密接に関連

- from: NE-05 WANボンディング
  to: CM-04 回線冗長化
  relation: WANボンディングは冗長化の具体的手法

- from: VT-05 NVIDIA Broadcast
  to: DO-03 VRAM最適化
  relation: GPU負荷の分析視点が共通

- from: DO-02 OBS WebSocket
  to: DO-01 Stream Deck
  relation: Stream DeckからWebSocket経由でOBS制御する場合に関連
```

## 3. プレイリスト構成案

<!--
YouTubeのプレイリストは、視聴者の学習パスとして機能します。
以下は推奨視聴順序に基づくプレイリスト設計案です。

プレイリスト内の動画は、PhaseやコンテンツIDの順番ではなく、
視聴者の理解が段階的に深まるよう、依存関係に基づいて配置しています。
-->

### PL-01: 配信トラブル即解決シリーズ

Phase 1のトラブルシューティング動画を集約。検索流入の受け皿となるプレイリスト。

1. AE-01 - OBS音ズレを根治する
2. NE-01 - 配信が止まる・カクつく原因の切り分け
3. VT-01 - VTube Studioパラメータスムージング
4. NE-06 - プラットフォーム再エンコードの罠
5. AE-03 - ノイズゲート最適化
6. VT-02 - OBS色空間・LUT設定の正解
7. NE-02 - CBRビットレート設計
8. CM-01 - OBSプロファイルをGitで管理する

### PL-02: 配信オーディオ完全攻略

オーディオドメインを基礎から応用まで体系的にカバー。

1. AE-01 - OBS音ズレを根治する
2. AE-02 - VST処理チェーン構築入門
3. AE-03 - ノイズゲート最適化
4. AE-04 - LUFS音圧最適化
5. AE-09 - スタンドアロンVSTホスト活用
6. AE-07 - Audio Ducking / Sidechain Compression
7. AE-05 - ASIO Routing実践
8. AE-06 - Hardware Loopback完全ガイド
9. AE-08 - Dante / Audio over IP

### PL-03: VTuberビジュアル・トラッキング講座

ビジュアル品質とトラッキング精度の向上を段階的に解説。

1. VT-01 - VTube Studioパラメータスムージング
2. VT-02 - OBS色空間・LUT設定の正解
3. VT-03 - iOS ARKit vs Webcamトラッキング
4. VT-04 - Blend Shapes完全解説
5. VT-05 - NVIDIA Broadcast GPU負荷ベンチマーク

### PL-04: 配信ネットワーク最適化

ネットワーク起因の問題解決から高度な最適化まで。

1. NE-01 - 配信が止まる・カクつく原因の切り分け
2. NE-06 - プラットフォーム再エンコードの罠
3. NE-02 - CBRビットレート設計
4. NE-03 - Ingest Server経路最適化
5. NE-04 - QoS設定実践ガイド
6. NE-05 - WANボンディング実践

### PL-05: 配信環境の構成管理と冗長化

安定した環境を維持し、障害に備える設計手法。

1. CM-01 - OBSプロファイルをGitで管理する
2. CM-02 - OBSポータブルモード運用
3. CM-03 - 2PC配信構成設計
4. CM-04 - 回線冗長化戦略

### PL-06: 配信DevOps - 自動化とモニタリング

配信オペレーションのエンジニアリング的アプローチ。

1. DO-01 - Stream Deck / Touch Portalマクロ構築
2. DO-02 - OBS WebSocket入門
3. DO-03 - VRAM Allocation最適化
4. DO-04 - Streamer.bot演出自動化
5. DO-05 - 配信システムモニタリング
6. DO-06 - YouTube API + Python自動化

## 4. 視聴者導線設計

<!--
「導線」とは、ある動画を見た視聴者が次にどの動画へ進むべきかの誘導経路です。
YouTube動画の終了画面（エンドスクリーン）やカード機能で実装します。

Phase 1 の動画からは、同じトピックの Phase 2 動画へ誘導することで、
チャンネル内の回遊率（視聴者が複数の動画を見る率）を高めます。
-->

### Phase 1 からの誘導パス

| Phase 1 動画 | 推奨次動画（同ドメイン深堀り） | 推奨次動画（関連ドメイン） |
| --- | --- | --- |
| AE-01 音ズレ根治 | AE-02 VST処理チェーン | NE-01 配信停止の切り分け |
| AE-02 VST処理チェーン | AE-09 スタンドアロンVSTホスト or AE-03 ノイズゲート | なし |
| AE-03 ノイズゲート | AE-04 LUFS | なし |
| AE-04 LUFS | AE-07 Audio Ducking | なし |
| VT-01 VTube Studio | VT-03 ARKit vs Webcam | AE-01 音ズレ根治 |
| VT-02 OBS色空間 | VT-05 NVIDIA Broadcast | NE-01 配信停止の切り分け |
| NE-01 配信停止切り分け | NE-02 CBR設計 | AE-01 音ズレ根治 |
| NE-02 CBR設計 | NE-03 Ingest Server | NE-06 プラットフォーム再エンコード |
| NE-06 プラットフォーム再エンコード | NE-02 CBR設計 | VT-02 OBS色空間 |
| CM-01 OBS Git管理 | CM-02 ポータブルモード | なし |
