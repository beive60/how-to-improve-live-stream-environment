# EP030 / AE-09: スタンドアロンVSTホスト活用 - OBSもDiscordも同時に音声加工する

<!--
このエピソードの核心:
AE-02（OBS VST2入門）は「OBS出力の音声品質改善」に閉じている。
しかし配信者の音声出力先はOBSだけではない。Discord、ゲーム内VC、
録画ソフト等、複数のアプリケーションが同時にマイク入力を参照している。

OBS VST2ホストでの音声加工は、OBS以外のアプリケーションには一切適用されない。
つまりコラボ配信時、配信視聴者には処理済みの高品質な音声が届く一方、
Discord相手（コラボ相手）には未処理の生マイク音声が聞こえている。
多くの配信者はこの非対称に気づいていない（unknown unknowns）。

スタンドアロンVSTホストはWindowsのオーディオデバイスレベルで音声を処理し、
全アプリケーションに処理済み音声を供給する。これはOBS VST2の「上位互換」ではなく、
音声処理のパラダイムが根本的に異なる。
-->

## 動画構成案

### フック（0:00-0:30）

- 「OBSで音声加工してるのに、Discordでは生マイクのまま。気づいてますか？」
- 2画面分割: 左 = 配信視聴者に聞こえる音声（処理済み）、右 = Discordのコラボ相手に聞こえる音声（未処理）
- この差を聴覚で体験させ、問題の深刻さを直感させる

### 課題の明確化（0:30-1:30）

- OBS VST2ホストの処理範囲を図解で示す（OBS内パイプラインのみ）
- 「Discordはマイクの生入力を参照している」という事実
- コラボ配信で発生する具体的な問題パターン:
  - 配信上はEQ/コンプで整った声、Discord相手にはこもった生マイク
  - 配信上はノイズゲートが効いている、Discord相手には環境音が聞こえる
  - コラボ相手の配信に載る自分の声が低品質になる

### ロードマップ提示（1:30-2:00）

1. OBS VST2ホストの処理範囲の限界
2. スタンドアロンVSTホストの仕組みと利点
3. Cantabile Liteによる構築手順
4. VoiceMeeter Insert経由の統合方法（既存VoiceMeeterユーザー向け）
5. ASIO移行パスへの展望

### 本編: OBS VST2の限界（2:00-4:00）

- OBS内蔵VSTホストの処理フロー図（マイク入力 → OBS VST → OBS出力のみ）
- Windows側のマイクデバイスは未加工のまま全アプリケーションに参照される
- OBS、Discord、ゲーム内VC、録画ソフトがそれぞれ独立してマイクにアクセスする図
- AE-02の内容を前提とし、「AE-02で構築したVSTチェーンはOBSの中でしか機能しない」を明確化

### 本編: スタンドアロンVSTホストの仕組み（4:00-7:00）

- VSTホストアプリケーション + 仮想オーディオデバイスの組み合わせ
- 音声フロー: 物理マイク → VSTホスト（VST処理チェーン） → 仮想オーディオデバイス → 全アプリケーション
- この構成では OBS、Discord、ゲーム内VC、録画ソフトの全てが処理済み音声を受け取る
- VSTホストの候補と比較:
  - Cantabile Lite（無料、VST2/VST3対応、低レイテンシー）
  - Element（無料、軽量）
  - Pedalboard 2（無料、シンプル）
- 仮想オーディオデバイスの候補:
  - VB-Audio Virtual Cable（無料）
  - VoiceMeeter内蔵の仮想入力（VoiceMeeter既存ユーザーの場合）

### 本編: Cantabile Liteによる構築デモ（7:00-11:00）

- Cantabile Liteのインストールと初期設定
- VSTプラグインの読み込み（AE-02で使用したEQ/コンプ/リミッターをそのまま適用）
- VB-Audio Virtual Cableのインストールと設定
- 物理マイク → Cantabile → Virtual Cable の接続
- Windows既定のマイクデバイスをVirtual Cableに変更
- OBS、Discord両方で処理済み音声が入力されていることの確認デモ
- レイテンシーの計測と実用性の検証

### 本編: VoiceMeeter Insert統合（11:00-13:00）

- VoiceMeeter Banana/PotatoのInsert機能の概要
- Insert APIを通じたVSTホストとの接続方法
- VoiceMeeter既存ユーザーがスタンドアロンVSTホストを統合する手順
- 注意: VoiceMeeterのWindowsオーディオエンジン依存によるドライバ競合リスクに言及
- 長期的にはASIO直接ルーティング（AE-05）への移行を推奨する旨を明示

### 計測検証（13:00-14:30）

- OBS出力音声の波形比較（AE-02方式 vs AE-09方式: 品質同等であることの確認）
- Discord入力音声の波形比較（未処理 vs 処理済み: 改善の定量化）
- VSTホストのCPU負荷計測（システム監視ツールで実測）
- レイテンシー計測（スタンドアロンVSTホスト経由の追加遅延）

### まとめと次動画への誘導（14:30-15:30）

- 「音声処理をOBS内に閉じるか、システムワイドに開くか」という選択の整理
- OBS VST2（AE-02）: 最もシンプル。OBS出力のみで十分な場合
- スタンドアロンVSTホスト（本動画）: コラボ配信者、複数アプリ利用者向け
- ASIO Routing（AE-05）: 低遅延・高安定性を求めるプロシューマー向け
- End Screen: AE-05（ASIO Routing）への誘導

## 必要な動画素材

### 画面キャプチャ

- OBS音声フィルタ画面（AE-02との比較用）
- Cantabile Liteのメイン画面（VSTプラグイン読み込み、ルーティング設定）
- VB-Audio Virtual Cableの設定画面
- Windowsサウンド設定画面（既定のマイクデバイス変更）
- Discordの音声設定画面（入力デバイス選択）
- VoiceMeeter BananaのInsert設定画面
- タスクマネージャー/リソースモニターのCPU負荷表示

### デモ映像

- OBS VST2のみの構成でDiscordに入力される音声（未処理）のデモ
- スタンドアロンVSTホスト構成でDiscordに入力される音声（処理済み）のデモ
- A/B比較: 配信視聴者に聞こえる音声 vs Discordコラボ相手に聞こえる音声
- Cantabile Liteのセットアップ操作デモ
- VB-Audio Virtual Cableのセットアップ操作デモ
- VoiceMeeter Insert接続操作デモ

### 図解・テロップ素材

- 音声処理範囲の比較図（OBS VST2: OBS内のみ / VSTホスト: システムワイド）
- Windowsオーディオ処理フロー図（物理マイク → VSTホスト → 仮想デバイス → 各アプリ）
- VSTホストアプリ比較表（Cantabile Lite / Element / Pedalboard 2）
- VoiceMeeter Insert APIのデータフロー図

## 必要機材

### 所有済み

- マイク: Audio-Technica AT-2020
- オーディオIF: Roland VT-4
- PC2: RTX 3060（OBS + VSTホスト + Discord同時動作デモ用）

### 追加購入

なし。本エピソードはソフトウェア完結（Cantabile Lite、VB-Audio Virtual Cable、VoiceMeeter Banana: 全て無料）。

## SEOキーワード候補

- Discord マイク 音質
- コラボ配信 音声 設定
- VSTホスト 配信
- OBS VST Discord
- 配信 音声加工 全アプリ
- Cantabile 配信
- VoiceMeeter Insert VST

## 補足メモ

- AE-02（OBS VST2入門）の視聴を前提とするため、VSTプラグイン自体の解説は最小限に留める
- 動画内で明確にAE-02を参照し、「AE-02で学んだVSTチェーンをそのまま使える」ことを示す
- VoiceMeeter Insertセクションでは、Overview.mdの方針（VoiceMeeterの推奨順位低下）と
  整合させ、「既にVoiceMeeterを使用している場合の実用的な経路」として提示する
- ASIO Routing（AE-05）への導線を明確に設け、「より安定した構成への進化」として位置づける
- サムネイル案: 左右分割で「OBS: 処理済み / Discord: 生マイク!?」の構図。
  ドメインカラーはAE（ダークブルー #1a237e）
