# Content Catalog

<!--
このファイルは、チャンネルで制作する全動画の企画一覧です。
Overview.md セクション6のコンテンツ例を「動画1本 = 1企画」の粒度に分解したものです。

コンテンツIDの体系:
  AE-XX : Audio Engineering（オーディオエンジニアリング / Overview 6.1）
  VT-XX : Visual & Tracking（ビジュアル・トラッキング / Overview 6.2）
  NE-XX : Network Engineering（ネットワークエンジニアリング / Overview 6.3）
  CM-XX : Configuration Management（構成管理と冗長化 / Overview 6.4）
  DO-XX : DevOps for Streamers（DevOps / Overview 6.5）

Phase の意味（Overview セクション10参照）:
  Phase 1 : トラブルシューティング系。検索流入を獲得するための初期コンテンツ。
             「OBS 音ズレ」「VTuber 重い」など、視聴者が今すぐ解決したい問題を扱う。
  Phase 2 : 体系的な技術解説シリーズ。ドメインごとの辞書的コンテンツ。
             Phase 1 で獲得した視聴者を深い知識へ誘導する役割。
  Phase 3 : 高度なカスタマイズと自動化。上級者向け。
             Phase 1・2 の視聴者が成長した先のコンテンツ。

制作ステータスの定義:
  未着手   : 企画のみ。台本・素材の準備を開始していない。
  企画中   : 台本の構成案や検証項目を整理している段階。
  制作中   : 台本執筆、検証・収録、編集のいずれかが進行中。
  レビュー : 完成版の最終チェック中。
  公開済み : YouTubeにアップロード済み。
  保留     : 何らかの理由で制作を一時停止している。

想定尺の目安:
  10-15分 : トラブルシューティング系。問題提起→原因→解決の流れで完結。
  15-25分 : 体系的な技術解説。原理説明→実演→検証結果の提示。
  20-30分 : 高度な構築・自動化。環境準備→実装→動作確認を含むため長め。
-->

## 企画一覧

### AE: オーディオエンジニアリング

<!-- このドメインは Phase 1 の中核。「音」の問題は配信者が最も頻繁に検索するトピック。 -->

```yaml
- id: AE-01
  title: "OBS音ズレを根治する - サンプリングレート統一とバッファサイズの正解"
  phase: 1
  duration: "10-15分"
  status: pending
  summary: >
    音ズレの原因をサンプリングレート不一致・バッファサイズ設定の観点で
    切り分け、再発防止を含めた根本解決を提示する
    2026/02/21現在、音ズレを再現できないため、再現環境の構築と検証が必要

- id: AE-02
  title: "VST処理チェーン構築入門 - EQ/コンプレッサー/リミッターで配信音声を整える"
  phase: 1
  duration: "15-20分"
  status: 未着手
  summary: >
    OBS内蔵フィルタではなくVSTプラグインを使った音声処理チェーンの設計と実装。
    各プラグインの役割と推奨パラメータを解説する

- id: AE-03
  title: "ノイズゲート最適化 - 環境音スペクトル分析に基づく閾値設定"
  phase: 1
  duration: "10-15分"
  status: 未着手
  summary: >
    「声が途切れる」「環境音が入る」問題に対し、スペクトルアナライザで
    環境音を計測し、適切なノイズゲート閾値を決定する手法を提示する

- id: AE-04
  title: "LUFS音圧最適化 - YouTubeの-14 LUFS基準に合わせる方法"
  phase: 1
  duration: "10-15分"
  status: 未着手
  summary: >
    YouTube配信/アーカイブにおけるラウドネス正規化の仕組みと、
    配信段階で-14 LUFSに最適化する計測・調整手順を解説する

- id: AE-05
  title: "ASIO Routing実践 - FL Studio ASIO/ASIO Link Proで低遅延ルーティングを実現する"
  phase: 2
  duration: "15-25分"
  status: 未着手
  summary: >
    Windowsオーディオエンジンを回避し、ASIOドライバによる低遅延・安定
    ルーティングを構築する。VoiceMeeter系との比較も含む

- id: AE-06
  title: "Hardware Loopback完全ガイド - DSP内蔵オーディオIFによるハードウェアルーティング"
  phase: 2
  duration: "20-25分"
  status: 未着手
  summary: >
    RME TotalMix FX等のDSP内蔵オーディオインターフェースを使い、
    ソフトウェアに依存しないハードウェアレベルのルーティングを構築する。
    複数機材を接続することで発生するグランドループノイズ（60Hzハム・うなり音）を
    unknown unknowns として取り上げ、原因となるGND電位差の仕組みを解説したうえで
    グランドループノイズアイソレーター（トランス分離型）による解消手順を実演する。
    ハードウェアルーティングの構築と同時にノイズ問題を根治するセクションとして配置し、
    アイソレーターが不要なケース（専用オーディオIFの使用）との比較も提示する

- id: AE-07
  title: "Audio Ducking / Sidechain Compression - ゲーム音をマイク音声に連動して自動減衰させる"
  phase: 2
  duration: "15-20分"
  status: 未着手
  summary: >
    サイドチェインコンプレッションの原理を解説し、OBS/VSTでゲーム音や
    BGMをマイク音声に合わせて自動的に下げる設定を実装する

- id: AE-08
  title: "Dante / Audio over IP - 2PC配信でのロスレス音声伝送"
  phase: 3
  duration: "20-30分"
  status: 未着手
  summary: >
    LANケーブルによるロスレス音声伝送プロトコル（Dante）の概要と、
    2PC配信環境での実装手順を解説する

- id: AE-09
  title: "スタンドアロンVSTホスト活用 - OBSもDiscordも同時に音声加工する"
  phase: 2
  duration: "15-20分"
  status: 未着手
  summary: >
    OBS内蔵VSTホスト（AE-02）はOBS出力にのみ作用し、Discordやゲーム内VCには
    未処理の生マイク音声が入力される。スタンドアロンVSTホスト（Cantabile Lite等）を
    Windowsオーディオデバイスとして構成することで、全アプリケーションに対して
    VST処理済み音声を一括供給する方法を解説する。VoiceMeeter Insert経由の
    統合方法もカバーし、ASIO移行パス（AE-05）への導線を設ける。
    コラボ配信者にとってのエコシステム的優位性を重点的に扱う
```

### VT: ビジュアル・トラッキングパイプライン

```yaml
- id: VT-01
  title: "VTube Studioパラメータスムージング - 機械的な動きを排除するチューニング"
  phase: 1
  duration: "10-15分"
  status: 未着手
  summary: >
    VTube Studioのスムージングパラメータを調整し、カクカクした機械的な
    トラッキング動作を自然な動きに改善する方法を解説する

- id: VT-02
  title: "OBS色空間・LUT設定の正解 - 601/709、Full/Partialの違いと適切な選択"
  phase: 1
  duration: "15-20分"
  status: 未着手
  summary: >
    「色がおかしい」「映像がくすむ」問題の原因である色空間設定の不一致を
    解説し、環境に応じた正しい設定を提示する

- id: VT-03
  title: "iOS ARKit vs Webcamトラッキング - ジッター計測による定量比較"
  phase: 2
  duration: "15-25分"
  status: 未着手
  summary: >
    Face ID（ARKit）とWebcamベースのトラッキング精度をジッター計測で
    定量的に比較し、投資対効果を客観的に評価する

- id: VT-04
  title: "Blend Shapes完全解説 - ARKit 52種パラメータの理解と最適化"
  phase: 2
  duration: "20-25分"
  status: 未着手
  summary: >
    ARKitが提供する52種類の表情筋パラメータ（Blend Shapes）それぞれの意味と、
    VTube Studio/Live2Dでの最適なマッピング方法を解説する

- id: VT-05
  title: "NVIDIA Broadcast GPU負荷ベンチマーク - AI処理の実測コスト"
  phase: 2
  duration: "15-20分"
  status: 未着手
  summary: >
    NVIDIA BroadcastのAIノイズキャンセリング・背景除去がGPU負荷に与える影響を、
    ゲーム・OBS同時使用時の実測データで検証する
```

### NE: ネットワークエンジニアリング

```yaml
- id: NE-01
  title: "配信が止まる・カクつく原因の切り分けガイド - ネットワーク診断フロー"
  phase: 1
  duration: "10-15分"
  status: 未着手
  summary: >
    フレームドロップが「PC負荷」なのか「ネットワーク」なのかを切り分ける
    診断フローチャートを提示し、各原因への対処法を示す

- id: NE-02
  title: "CBRビットレート設計 - ネットワーク変動に対するマージン計算"
  phase: 1
  duration: "15-20分"
  status: 未着手
  summary: >
    固定ビットレート（CBR）の設定値をネットワーク帯域とジッターから逆算する
    手法を解説し、安定配信に必要なマージンを定量化する

- id: NE-03
  title: "Ingest Server経路最適化 - RTMPSサーバーへのTraceroute分析"
  phase: 2
  duration: "15-20分"
  status: 未着手
  summary: >
    YouTube/TwitchのIngestサーバーまでのネットワーク経路をTracerouteで分析し、
    最適なサーバー選択とボトルネック特定の手法を解説する

- id: NE-04
  title: "QoS設定実践ガイド - ルーターレベルのパケット優先制御"
  phase: 2
  duration: "15-25分"
  status: 未着手
  summary: >
    家庭用ルーターでQoS（Quality of Service）を設定し、
    配信トラフィックに優先順位を付ける方法を実機で解説する

- id: NE-05
  title: "WANボンディング実践 - Speedify等による回線冗長化"
  phase: 3
  duration: "20-25分"
  status: 未着手
  summary: >
    光回線+モバイルテザリング等、複数回線を束ねるWANボンディングの仕組みと、
    Speedifyを使った冗長化の実装手順を解説する

- id: NE-06
  title: "プラットフォーム再エンコードの罠 - YouTube AV1/VP9選択の仕組みとTwitch解像度戦略"
  phase: 1
  duration: "15-20分"
  status: 未着手
  summary: >
    YouTubeサーバー側の再エンコードでAV1が選択されると、高モーションのゲーム配信で
    ブロックノイズが発生して視聴体験が劣化する。1080p超の解像度でVP9を強制する
    テクニックと、Twitchにおける900p/8Mbpsのビットレート効率化戦略を解説する。
    配信者の多くが認識していないunknown unknownsに属するトピック
```

### CM: 構成管理と冗長化設計

<!--
このドメインは他のドメインと異なり、「いま困っている問題を解決する」類ではなく
「将来の問題を予防する」類のコンテンツ。Phase 1 に入れるのは CM-01 のみだが、
配信者が設定を壊してしまうトラブルは頻繁にあるため、検索需要はある。
-->

```yaml
- id: CM-00
  title: "配信PC ファイル管理の正解 - OBSソースが消えない設計とSSD/HDD使い分け"
  phase: 1
  duration: "10-15分"
  status: 未着手
  summary: >
    OBSは素材ファイル（オーバーレイ画像・BGM・動画）を絶対パスで参照するため、
    フォルダを移動・整理するだけで配信直前にシーンのソースが失われる。
    この問題を「ファイル管理設計の不在」として定義し、配信環境に特化した
    ホームディレクトリ構造の標準化、SSD（Cドライブ）への参照ファイル集約
    （HDDの読み込み遅延が演出タイミングのずれを引き起こす問題を含む）、
    Windowsジャンクションを使ったパス固定の手法を解説する。
    ファイル名規則（日付・バージョン表記の統一）も合わせて取り上げ、
    CM-01（Gitによる設定管理）へのファイルパス設計前提を整備する

- id: CM-01
  title: "OBSプロファイルをGitで管理する - 設定のバージョニングと安全な復元"
  phase: 1
  duration: "10-15分"
  status: 未着手
  summary: >
    OBSのプロファイル/シーンコレクションをGitで管理し、設定変更の追跡と
    任意時点への復元を可能にする手順を解説する

- id: CM-02
  title: "OBSポータブルモード運用 - レジストリ汚染回避と環境分離"
  phase: 2
  duration: "10-15分"
  status: 未着手
  summary: >
    OBSをポータブルモードで運用することでレジストリへの依存を排除し、
    複数環境の共存や安全なバックアップを実現する方法を解説する

- id: CM-03
  title: "2PC配信構成設計 - NDI/Capture Cardによる負荷分散とフェイルオーバー"
  phase: 3
  duration: "20-30分"
  status: 未着手
  summary: >
    ゲーミングPCと配信PCを分離するN+1構成の設計と、
    NDI/キャプチャカードそれぞれの実装方法、フェイルオーバー設計を解説する

- id: CM-04
  title: "回線冗長化戦略 - バックアップ接続の設計と自動切替"
  phase: 3
  duration: "15-20分"
  status: 未着手
  summary: >
    メイン回線障害時のバックアップ接続設計と、
    検知・切替の自動化手法を解説する

- id: CM-05
  title: "2PC間ファイル自動同期 - Windows共有とSyncTrayzorで素材・設定を統合管理する"
  phase: 3
  duration: "10-15分"
  status: 未着手
  summary: >
    2PC配信環境でOBSオーバーレイ・LUT・VSTプリセット・スクリプト等を
    両PCから参照・更新できる状態にするための同期構成を解説する。
    WindowsのSMBファイル共有（ホスト依存・設定が簡素）とSyncTrayzor/Syncthing
    （P2P・双方向・オフラインコピー保持）を比較し、用途に応じた選択基準を提示する。
    unknown unknownsに属するトピックであり、2PC構成を運用し始めて初めて問題と認識する性質上、
    CM-03のEnd Screen経由でのセッション内誘導を主要な流入経路とする

- id: CM-06
  title: "配信環境 PC移行完全ガイド - VTube Studio・OBS・Live2Dモデルを新PCに完全移行する手順"
  phase: 2
  duration: "15-20分"
  status: 未着手
  summary: >
    PC買い替え・OS再インストール時に必要な配信環境の完全移行手順を解説する。
    移行対象ファイルの棚卸し（Live2Dモデルのファイル構成・VTube Studioパラメータの
    保存場所・OBSプロファイルのパス）を丁寧に整理したうえで、旧PCから新PCへの
    実演手順と移行後の動作検証を示す。動画後半で「事前バックアップがあれば30分で
    完了する」ことを実証し、CM-07（自動バックアップ構築）への導線を設ける。
    「VTube Studio 設定 移行」「OBS PC 引き継ぎ」等の検索キーワードで流入を確保し、
    潜在的なバックアップニーズを顕在化させるファネルエントリーとして機能する
```

### DO: DevOps for Streamers

<!--
DO（DevOps）は Phase 2-3 が中心。
配信のオペレーションを自動化・効率化するコンテンツは、
基本的な配信環境が安定した後に視聴されるため、優先度は後回し。
ただし DO-01（Stream Deck）は Phase 1 の視聴者にも訴求力がある。
-->

```yaml
- id: DO-01
  title: "Stream Deck / Touch Portalマクロ構築 - ワンオペ配信の効率化"
  phase: 2
  duration: "15-20分"
  status: 未着手
  summary: >
    物理デバイス（Stream Deck）やソフトウェア（Touch Portal）でマクロを構築し、
    シーン切替・音声制御を1ボタンで実行する方法を解説する

- id: DO-02
  title: "OBS WebSocket入門 - 外部プログラムからのOBS制御基礎"
  phase: 2
  duration: "15-20分"
  status: 未着手
  summary: >
    OBS WebSocket APIの概要と基本的な制御方法を解説する。
    後続の自動化コンテンツ（DO-04）の前提知識となる

- id: DO-03
  title: "VRAM Allocation最適化 - ゲームとOBSのGPUリソース配分"
  phase: 2
  duration: "15-20分"
  status: 未着手
  summary: >
    ゲームとOBSが競合するVRAMリソースの優先順位付けと、
    GPU負荷を最適化する設定手法を実測データで解説する

- id: DO-04
  title: "Streamer.bot演出自動化 - OBS WebSocket連携による配信演出の自動制御"
  phase: 3
  duration: "20-25分"
  status: 未着手
  summary: >
    OBS WebSocketとStreamer.bot（旧LioranBoard）を連携させ、
    チャットイベント連動の演出自動化を実装する

- id: DO-05
  title: "配信システムモニタリング - Grafana + InfluxDBによるリソース可視化"
  phase: 3
  duration: "20-30分"
  status: 未着手
  summary: >
    CPU/GPU/ネットワーク使用率を時系列で記録・可視化するモニタリング環境を
    構築し、配信中のパフォーマンス問題を事後分析可能にする

- id: DO-06
  title: "YouTube API + Python自動化 - コメント分析と運用効率化"
  phase: 3
  duration: "20-25分"
  status: 未着手
  summary: >
    YouTube Data APIをPythonで操作し、コメント取得・センチメント分析・
    配信メタデータ管理を自動化する方法を解説する
```

## サマリー

| ドメイン | Phase 1 | Phase 2 | Phase 3 | 合計 |
| --- | --- | --- | --- | --- |
| AE: オーディオ | 4本 | 4本 | 1本 | 9本 |
| VT: ビジュアル | 2本 | 3本 | 0本 | 5本 |
| NE: ネットワーク | 3本 | 2本 | 1本 | 6本 |
| CM: 構成管理 | 2本 | 2本 | 2本 | 6本 |
| DO: DevOps | 0本 | 3本 | 3本 | 6本 |
| **合計** | **11本** | **14本** | **7本** | **32本** |

<!--
Phase 1 が 11本で最も多いのは意図的。
Phase 1 は「検索流入の獲得」が目的なので、
質の高いコンテンツを集中的に制作し、
チャンネルの信頼性を早期に確立することを優先する。
NE-06（プラットフォーム再エンコード）は unknown unknowns 型の
強力な差別化コンテンツとして追加。
-->
