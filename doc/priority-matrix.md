# 1. Priority Matrix

<!--
このファイルは、コンテンツカタログの各動画に対して
「どの順番で制作すべきか」を判断するための優先度評価表です。

3つの評価軸で各動画をスコアリングし、制作順序の意思決定に使います。
スコアは絶対的な正解ではなく、判断の叩き台として使ってください。
状況が変わったら（例: 新しいOBSアップデートで特定トピックの需要が急増）
スコアを見直して制作順序を調整します。
-->

## 1.1. 評価軸の定義

<!--
この4軸は Overview.md の差別化戦略と channel-growth-strategy.md の
アルゴリズム最適化戦略から導出しています。
Phase 1 は「検索流入の獲得」が目的なので検索需要の重みを最も高くしています。
アルゴリズム適合性はチャンネルリセット後の初動戦略として重要であり、
CTRの取りやすさ、視聴維持率の確保しやすさ、セッション時間への貢献を評価します。
-->

| 評価軸 | 説明 | スコア基準 |
| --- | --- | --- |
| 検索需要 | そのトピックを検索している人がどれだけいるか | H(3): 月間検索ボリュームが大きい、SNSでの質問頻度が高い / M(2): 一定の需要がある / L(1): ニッチな需要 |
| 制作容易性 | 制作に必要な時間・機材・検証コスト | H(3): 自宅環境で短期間に制作可能 / M(2): 一定の検証・準備が必要 / L(1): 特殊機材や長期検証が必要 |
| 差別化効果 | 既存の競合コンテンツと比較した独自性 | H(3): 同等の情報源がほぼ存在しない / M(2): 存在するが質が低い / L(1): 類似コンテンツが既に充実 |
| アルゴリズム適合性 | CTRの取りやすさ、視聴維持率の確保しやすさ、セッション時間への貢献 | H(3): 痛みが明確でサムネが作りやすく、解決まで見る動機が強い / M(2): 関心は引けるが維持率確保に工夫が必要 / L(1): ニッチすぎてインプレッションが伸びにくい |

<!--
「アルゴリズム適合性」は以下の3要素の総合評価:
  1. CTRポテンシャル: サムネイル/タイトルで「押したくなる」構図が作れるか
  2. 維持率ポテンシャル: 「問題→解決」の明確なストーリーラインがあるか
  3. セッション貢献: 次の動画への自然な導線が存在するか

チャンネルリセット後の初動では、アルゴリズムに「このチャンネルは価値がある」と
学習させることが最重要。そのため、初期はCTRと維持率が高くなりやすい
「痛みの明確な問題解決型」動画を優先する。
-->

### 1.1.1. スコア計算

<!--
重み付けの理由:
  検索需要 x2 : Phase 1 の主目的が検索流入の獲得であるため、最重要。
  制作容易性 x1 : 制作リソースが限られている個人制作のため考慮。
  差別化効果 x1.5 : チャンネルのポジショニングを確立するために重要。
  アルゴリズム適合性 x1.5 : チャンネルリセット後の初動では、アルゴリズムに好まれる動画を
  優先することがチャンネル成長の分水嶺となるため、差別化効果と同等の重み。

計算式: (検索需要 x 2) + (制作容易性 x 1) + (差別化効果 x 1.5) + (アルゴリズム適合性 x 1.5)
最大スコア: (3 x 2) + (3 x 1) + (3 x 1.5) + (3 x 1.5) = 18.0
-->

Phase 1 と Phase 2 の動画を同一の評価軸でスコアリングし、総合的な優先度ランクを決定します。

Score = (検索需要 x 2) + (制作容易性 x 1) + (差別化効果 x 1.5) + (アルゴリズム適合性 x 1.5)

| 優先度ランク | スコア範囲 | 意味 |
| --- | --- | --- |
| **S** | 15.0 以上 | 最優先。チャンネルリセット後の初動で公開すべき動画 |
| **A** | 12.0 - 14.5 | 高優先。Phase 1 の中盤以降で制作 |
| **B** | 9.0 - 11.5 | 通常優先。Phase 2 で制作 |
| **C** | 9.0 未満 | 低優先。需要や状況を見て判断 |

Phase 3 の動画はビジネスインパクトの評価も加味して別途評価します。

Score = (検索需要 × 2) + (制作容易性 × 1) + (差別化効果 × 1.5) + (アルゴリズム適合性 × 1.5) +(ビジネスインパクト × k)

## 1.2. Phase 1 優先度評価

<!--
Phase 1の中での制作順序を決めるための評価です。
Phase 1 の動画は全て「トラブルシューティング/検索流入獲得」が目的なので、
検索需要が高い動画から着手すべきです。

目安として、最初の3-4本で「このチャンネルは信頼できる」と
視聴者に認識してもらうことが重要です。
-->

```yaml
- id: AE-01
  title: "OBS音ズレ根治"
  search_demand: H  # 3
  ease_of_production: H  # 3
  differentiation: H  # 3
  algorithm_fit: H  # 3 - 痛みが明確、サムネでBefore/Afterが作りやすい、解決まで見る動機が強い
  score: 18.0
  rank: S

- id: NE-01
  title: "配信停止の切り分け"
  search_demand: H  # 3
  ease_of_production: H  # 3
  differentiation: M  # 2
  algorithm_fit: H  # 3 - 「配信が止まる」は緊急性が高く、クリック動機が最も強い
  score: 16.5
  rank: S

- id: VT-01
  title: "VTube Studioスムージング"
  search_demand: H  # 3
  ease_of_production: H  # 3
  differentiation: M  # 2
  algorithm_fit: H  # 3 - VTuberターゲットへの直接訴求、トピック学習に最適
  score: 16.5
  rank: S

- id: AE-03
  title: "ノイズゲート最適化"
  search_demand: H  # 3
  ease_of_production: H  # 3
  differentiation: M  # 2
  algorithm_fit: M  # 2 - 問題は明確だがスペクトル分析のビジュアルがやや地味
  score: 15.0
  rank: S

- id: AE-04
  title: "LUFS音圧最適化"
  search_demand: M  # 2
  ease_of_production: H  # 3
  differentiation: H  # 3
  algorithm_fit: M  # 2 - YouTube基準という明確なゴールがあるが、視覚的インパクトは中程度
  score: 14.5
  rank: A

- id: AE-02
  title: "VST処理チェーン"
  search_demand: M  # 2
  ease_of_production: M  # 2
  differentiation: H  # 3
  algorithm_fit: M  # 2 - 「音質改善」は興味を引くが、専門的な印象でCTRに工夫が必要
  score: 13.0
  rank: A

- id: VT-02
  title: "OBS色空間/LUT"
  search_demand: M  # 2
  ease_of_production: M  # 2
  differentiation: H  # 3
  algorithm_fit: H  # 3 - 「色がおかしい」の痛みが明確、Before/Afterのビジュアルインパクトが強い
  score: 14.5
  rank: A

- id: NE-02
  title: "CBRビットレート設計"
  search_demand: M  # 2
  ease_of_production: M  # 2
  differentiation: H  # 3
  algorithm_fit: M  # 2 - 「ビットレート」検索は多いが、設計覚のタイトルは初心者を遠ざけるリスク
  score: 13.0
  rank: A

- id: CM-01
  title: "OBS Git管理"
  search_demand: L  # 1
  ease_of_production: H  # 3
  differentiation: H  # 3
  algorithm_fit: L  # 1 - ニッチすぎてインプレッションが伸びない、初動に不向き
  score: 10.5
  rank: B

- id: NE-06
  title: "プラットフォーム再エンコード"
  search_demand: H  # 3 - 「配信 画質 悪い」「YouTube ブロックノイズ」は高頻度クエリ。症状の検索需要が大きい
  ease_of_production: H  # 3 - OBS設定 + YouTube Stats for Nerds + 比較映像のみ。特殊機材不要
  differentiation: H  # 3 - unknown unknowns領域。日本語圏に同等の解説がほぼ存在しない
  algorithm_fit: H  # 3 - 「隠れた原因」フックで強力なCTR。Before/After比較映像で維持率確保が容易。NE-02への自然な導線
  score: 18.0
  rank: S
  note: >
    AE-01と同率首位。ただし性質が異なる。AE-01は「既知の痛み（音ズレ）への解決策」
    であるのに対し、NE-06は「未知の原因（AV1再エンコード）の暴露」。
    この「unknown unknowns」型コンテンツはチャンネルの技術的権威性を
    一段引き上げる差別化効果を持つ

- id: AE-10
  title: "AIノイズキャンセリング"
  search_demand: H  # 3 - 「NVIDIA Broadcast 配信」「RTX Voice 設定」「配信 ノイズ除去」は高頻度検索
  ease_of_production: H  # 3 - NVIDIA製GPU環境があれば実装可能、設定もシンプル、特殊機材不要
  differentiation: M  # 2 - NVIDIA Broadcast関連コンテンツは既存あり、定量的比較や詳細設定解説は少ない
  algorithm_fit: H  # 3 - 「ノイズが消える」Before/Afterが明確、サムネが作りやすく視聴維持率も確保しやすい
  score: 16.5
  rank: S
  note: >
    VT-01、NE-01と同スコア。AE-03（ノイズゲート）の代替/補完アプローチとして位置づけ。
    ハードウェアフィルタ（ノイズゲート）とAI処理（Broadcast）の比較により、
    視聴者に選択肢を提示する。VT-05（GPU負荷ベンチマーク）への導線も機能する
```

### 1.2.1. Phase 1 推奨制作順序

<!--
この制作順序は、依存関係マップ（dependency-map.md）の前提関係と、
channel-growth-strategy.md のアルゴリズム初動戦略も考慮しています。

最初の3本は Sランクから選出し、全て異なるドメインから出す。
これにより、アルゴリズムに「このチャンネルはVTuber配信環境全般をカバーする」と
学習させつつ、トピック一貫性を維持する。

4本目に NE-06（unknown unknowns型）を配置することで、
「既知の問題を解決するチャンネル」から「隠れた問題を暴くチャンネル」へ
視聴者の認識を引き上げる。この順序が技術的権威の早期確立に最適。

また、初動5本の期間は、各動画の公開後48時間のパフォーマンスを
最大化するために、SNS/コミュニティでの外部シグナル注入を役割とする。
-->

```yaml
- order: 1
  id: AE-01
  title: "OBS音ズレ根治"
  rank: S
  rationale: >
    最高スコア。全評価軸が最高評価。
    チャンネルリセット後の第1弾として、「定量的データに基づく技術解説」の
    スタイルを確立する。アルゴリズムに最初の「成功シグナル」を送る最重要動画

- order: 2
  id: NE-01
  title: "配信停止の切り分け"
  rank: S
  rationale: >
    音ズレと並ぶ最頻出トラブル。AE-01と異なるドメインを扱うことで
    チャンネルの幅を示す。緊急性の高い問題でCTRが取りやすい

- order: 3
  id: VT-01
  title: "VTube Studioスムージング"
  rank: S
  rationale: >
    VTuber特化の技術解説。3本目で「VTuber配信環境」という
    チャンネルのトピックをアルゴリズムに明確に学習させる

- order: 4
  id: NE-06
  title: "プラットフォーム再エンコード"
  rank: S
  rationale: >
    AE-01と同率のS最高スコア。初動3本で「既知の問題を解決するチャンネル」の
    信頼を確立した直後に「unknown unknowns爆弾」を投下する。
    「視聴者が知らない画質劣化の原因」というフックは、チャンネルの技術的権威を
    一段引き上げる。制作容易性もHであり初動の制作負荷を圧迫しない

- order: 5
  id: AE-03
  title: "ノイズゲート最適化"
  rank: S
  rationale: >
    オーディオドメインの追加動画。AE-02（VSTチェーン）が本来の前提だが、
    ノイズゲート単体でも理解可能な構成にすることで早期公開を優先

- order: 6
  id: AE-10
  title: "AIノイズキャンセリング"
  rank: S
  rationale: >
    AE-03（ノイズゲート）の次に配置し、ノイズ対策の2つのアプローチ
    （ハードウェアフィルタ vs AI処理）を連続して提示することで、
    視聴者に選択肢を与える。検索需要・制作容易性・アルゴリズム適合性が全てH。
    NVIDIA BroadcastのGPU負荷懸念から、VT-05（GPU負荷ベンチマーク）への
    自然な導線を構築できる

- order: 7
  id: VT-02
  title: "OBS色空間/LUT"
  rank: A
  rationale: >
    Before/Afterのビジュアルインパクトが強く、CTRが取りやすい。
    差別化効果が高く、競合が少ないトピック

- order: 8
  id: AE-04
  title: "LUFS音圧最適化"
  rank: A
  rationale: >
    YouTube基準（-14 LUFS）という明確なゴールがあり、
    動画内での結論が明快。差別化効果が高い

- order: 9
  id: AE-02
  title: "VST処理チェーン"
  rank: A
  rationale: >
    AE-03、AE-04の前提知識。体系的解説の基盤を作る。
    アルゴリズム適合性はやや劣るが、チャンネルの知識体系構築に不可欠

- order: 10
  id: NE-02
  title: "CBRビットレート設計"
  rank: A
  rationale: >
    NE-01の深掘り。NE-06（プラットフォーム再エンコード）との補完関係があり、
    「ローカル側のビットレート設計」と「プラットフォーム側の再エンコード挙動」を
    セットで理解させるセッション設計

- order: 11
  id: CM-01
  title: "OBS Git管理"
  rank: B
  rationale: >
    検索需要は低いが差別化効果は最高。Phase 1の締めとして独自性を示す
```

## 1.3. Phase 2 優先度評価

<!--
Phase 2 は体系的な技術解説シリーズ。
Phase 1 で獲得した視聴者を深い知識へ誘導する役割があるため、
Phase 1 動画との関連性も考慮して順序を決めます。
Phase 2 の制作は Phase 1 が概ね完了してから着手することを前提としています。
-->

```yaml
- id: AE-09
  title: "スタンドアロンVSTホスト"
  search_demand: H  # 3 - 「Discord 音質」「コラボ配信 マイク」「VSTホスト 配信」は高頻度。コラボ配信者の実用痛点
  ease_of_production: H  # 3 - 無料ソフトウェア完結（Cantabile Lite等）。特殊機材不要
  differentiation: H  # 3 - OBS VST2とスタンドアロンVSTホストのエコシステム差異を体系的に解説する日本語コンテンツはほぼ存在しない
  algorithm_fit: H  # 3 - 「OBSで音声加工してるのにDiscordでは生マイク」フックが強力。コラボ配信者への直接訴求でCTRが高い
  score: 18.0
  rank: S
  note: >
    Phase 2の中で唯一のSランク。AE-02（OBS VST2）の上位ステップとしての
    位置づけだが、本質的な価値は「OBS内に閉じた音声処理」から
    「全アプリケーションへの音声供給」へのパラダイム転換にある。
    コラボ配信者にとっては、Discord相手に聞こえる自分の声が未処理であるという
    unknown unknowns的な問題を暴露する点で、NE-06と同質の差別化効果を持つ

- id: AE-05
  title: "ASIO Routing"
  search_demand: M  # 2
  ease_of_production: M  # 2
  differentiation: H  # 3
  algorithm_fit: M  # 2 - 専門的だがVoiceMeeterとの比較で関心を引ける
  score: 13.0
  rank: A

- id: AE-07
  title: "Audio Ducking"
  search_demand: M  # 2
  ease_of_production: M  # 2
  differentiation: H  # 3
  algorithm_fit: M  # 2 - 配信中の実用性が高く関心を引く
  score: 13.0
  rank: A

- id: VT-03
  title: "ARKit vs Webcam"
  search_demand: M  # 2
  ease_of_production: L  # 1
  differentiation: H  # 3
  algorithm_fit: H  # 3 - 比較検証はサムネが作りやすくCTRが高い
  score: 14.0
  rank: A

- id: DO-01
  title: "Stream Deck マクロ"
  search_demand: M  # 2
  ease_of_production: H  # 3
  differentiation: M  # 2
  algorithm_fit: M  # 2 - ガジェット系は一定の関心がある
  score: 12.0
  rank: A

- id: DO-02
  title: "OBS WebSocket入門"
  search_demand: L  # 1
  ease_of_production: M  # 2
  differentiation: H  # 3
  algorithm_fit: L  # 1 - 開発者向けでインプレッションが限定的
  score: 10.0
  rank: B

- id: DO-03
  title: "VRAM Allocation"
  search_demand: M  # 2
  ease_of_production: M  # 2
  differentiation: H  # 3
  algorithm_fit: H  # 3 - 「ゲームが重い」「OBSがカクつく」の痛みに直結、CTRが取れる
  score: 14.5
  rank: A

- id: AE-06
  title: "Hardware Loopback"
  search_demand: L  # 1
  ease_of_production: L  # 1
  differentiation: H  # 3
  algorithm_fit: L  # 1 - 特定機材前提で視聴者が限定される
  score: 9.0
  rank: B

- id: VT-04
  title: "Blend Shapes"
  search_demand: L  # 1
  ease_of_production: M  # 2
  differentiation: H  # 3
  algorithm_fit: M  # 2 - ARKitユーザーには強い関心だが層が限定的
  score: 11.0
  rank: B

- id: VT-05
  title: "NVIDIA Broadcast"
  search_demand: M  # 2
  ease_of_production: M  # 2
  differentiation: M  # 2
  algorithm_fit: H  # 3 - AI技術のベンチマークは関心度が高い
  score: 13.0
  rank: A

- id: NE-03
  title: "Ingest Server"
  search_demand: L  # 1
  ease_of_production: M  # 2
  differentiation: H  # 3
  algorithm_fit: L  # 1 - ニッチすぎて広範なインプレッションが難しい
  score: 9.5
  rank: B

- id: NE-04
  title: "QoS設定"
  search_demand: L  # 1
  ease_of_production: L  # 1
  differentiation: H  # 3
  algorithm_fit: L  # 1 - ネットワーク層の話題でインパクトが弱い
  score: 9.0
  rank: B

- id: CM-02
  title: "OBSポータブルモード"
  search_demand: L  # 1
  ease_of_production: H  # 3
  differentiation: H  # 3
  algorithm_fit: L  # 1 - 予防系コンテンツで緊急性が低くクリック動機が弱い
  score: 10.5
  rank: B
```

### 1.3.1. Phase 2 推奨制作順序

<!--
Phase 2 の制作順序は、Phase 1 で獲得した視聴者層の関心と、
技術解説の体系性を両立させることを重視しています。

最もスコアの高い動画から着手し、視聴者の関心が高いトピックを優先します。
また、Phase 1 で扱った内容との関連性も考慮し、自然な知識の深掘りを促す構成とします。
-->

```yaml
- order: 1
  id: AE-09
  title: "スタンドアロンVSTホスト"
  rank: S
  rationale: >
    Phase 2 最高スコア（18.0）。Phase 1 の AE-02（OBS VST2入門）で獲得した
    視聴者に対し、「OBSの中だけで加工しても、Discordには生マイクが入力される」
    というunknown unknowns的な問題を暴露する。コラボ配信者への直接訴求力が高く、
    制作容易性もH（無料ソフトウェア完結）。Phase 2の1本目として
    オーディオドメインの権威性を一段引き上げる

- order: 2
  id: DO-03
  title: "VRAM Allocation"
  rank: A
  rationale: >
    Phase 2 Aランク最高スコア。「ゲームが重い」「OBSがカクつく」という
    具体的な痛みに直結し、CTRとアルゴリズム適合性が高い。
    Phase 1 の視聴者が次に求める実用的な最適化情報

- order: 3
  id: VT-03
  title: "ARKit vs Webcam"
  rank: A
  rationale: >
    比較検証コンテンツはサムネが作りやすくCTRが高い。
    Phase 1 の VT-01（スムージング）からの自然な流れで、
    トラッキング方式の選択という次のステップを提示

- order: 4
  id: AE-05
  title: "ASIO Routing"
  rank: A
  rationale: >
    Phase 1 のオーディオ系動画（AE-01, AE-03, AE-04）で獲得した視聴者への
    次のステップ。AE-09（VSTホスト）からの導線も機能する。
    VoiceMeeterとの比較で差別化効果が高い

- order: 5
  id: AE-07
  title: "Audio Ducking"
  rank: A
  rationale: >
    配信中の実用性が高く、オーディオドメインの体系化を進める。
    AE-02（VSTチェーン）、AE-09（VSTホスト）、AE-05（ASIO Routing）との
    自然な関連性

- order: 6
  id: VT-05
  title: "NVIDIA Broadcast"
  rank: A
  rationale: >
    AI技術のベンチマークは関心度が高い。VTuberドメインの
    技術解説を充実させ、Phase 1 で確立したトピックを強化

- order: 7
  id: DO-01
  title: "Stream Deck マクロ"
  rank: A
  rationale: >
    ガジェット系は一定の関心があり、制作容易性も高い。
    DevOpsドメインの入門として位置づけ、Phase 3 への橋渡し

- order: 8
  id: VT-04
  title: "Blend Shapes"
  rank: B
  rationale: >
    VT-03（ARKit vs Webcam）の深掘り。ARKitユーザーには強い関心があり、
    VTuberドメインの体系的コンテンツを完成させる

- order: 9
  id: CM-02
  title: "OBSポータブルモード"
  rank: B
  rationale: >
    Phase 1 の CM-01（OBS Git管理）と合わせて、
    コンフィグ管理シリーズを完成させる。制作容易性が高い

- order: 10
  id: DO-02
  title: "OBS WebSocket入門"
  rank: B
  rationale: >
    DO-01（Stream Deck）からの自然な流れ。開発者向けだが、
    Phase 3 の自動化コンテンツへの前提知識として必要

- order: 11
  id: NE-03
  title: "Ingest Server"
  rank: B
  rationale: >
    Phase 1 の NE-01, NE-02 の深掘り。ニッチだが
    ネットワークドメインの体系的コンテンツを構築

- order: 12
  id: AE-06
  title: "Hardware Loopback"
  rank: B
  rationale: >
    オーディオドメインの高度なトピック。特定機材前提だが、
    Phase 1-2 のオーディオシリーズの完結編として位置づけ

- order: 13
  id: NE-04
  title: "QoS設定"
  rank: B
  rationale: >
    ネットワークドメインの完結編。Phase 2 の締めとして
    全ドメインの体系的解説を完成させる
```

## 1.4. Phase 3 優先度評価

<!--
Phase 3 は高度なカスタマイズと自動化。
Phase 1-2 の視聴者データ（どの動画が人気か、コメントでの要望等）を見てから
制作順序を最終決定することを推奨します。
ここでのスコアは暫定評価としてください。
-->

```yaml
- id: DO-04
  title: "Streamer.bot自動化"
  search_demand: M  # 2
  ease_of_production: M  # 2
  differentiation: H  # 3
  algorithm_fit: M  # 2 - 自動化は関心を引くが前提知識が多い
  score: 13.0
  rank: A

- id: AE-08
  title: "Dante / AoIP"
  search_demand: L  # 1
  ease_of_production: L  # 1
  differentiation: H  # 3
  algorithm_fit: L  # 1 - プロ向け機材前提で視聴者が極めて限定的
  score: 9.0
  rank: B

- id: CM-03
  title: "2PC配信構成"
  search_demand: M  # 2
  ease_of_production: L  # 1
  differentiation: H  # 3
  algorithm_fit: M  # 2 - 2PC構成は関心が高いが実装が重い
  score: 12.0
  rank: A

- id: CM-04
  title: "回線冗長化"
  search_demand: L  # 1
  ease_of_production: M  # 2
  differentiation: M  # 2
  algorithm_fit: L  # 1 - 予防系コンテンツでクリック動機が弱い
  score: 7.5
  rank: C

- id: NE-05
  title: "WANボンディング"
  search_demand: L  # 1
  ease_of_production: M  # 2
  differentiation: M  # 2
  algorithm_fit: L  # 1 - ニッチすぎてインプレッションが伸びない
  score: 7.5
  rank: C

- id: DO-05
  title: "Grafana監視"
  search_demand: L  # 1
  ease_of_production: L  # 1
  differentiation: H  # 3
  algorithm_fit: M  # 2 - ダッシュボードのビジュアルはサムネ映えする
  score: 10.5
  rank: B

- id: DO-06
  title: "YouTube API自動化"
  search_demand: L  # 1
  ease_of_production: M  # 2
  differentiation: M  # 2
  algorithm_fit: L  # 1 - プログラマー向けで層が限定される
  score: 7.5
  rank: C
```

### 1.4.1. Phase 3 推奨制作順序

<!--
Phase 3 は高度なカスタマイズと自動化のフェーズです。
Phase 1-2 の視聴者データ（どの動画が人気か、コメントでの要望等）を
分析した上で、最終的な制作順序を調整することを推奨します。

ここでの順序はスコアと Phase 1-2 との関連性を基準とした暫定案です。
視聴者の反応に応じて柔軟に変更してください。

Score=(検索需要×2)+(制作容易性×1)+(差別化効果×1.5)+(アルゴリズム適合性×1.5)+(ビジネスインパクト×k)

-->

```yaml
- order: 1
  id: DO-04
  title: "Streamer.bot自動化"
  rank: A
  rationale: >
    Phase 3 最高スコア。Phase 2 の DO-01（Stream Deck）、
    DO-02（OBS WebSocket）からの自然な流れ。
    自動化への関心は高く、DevOpsドメインの集大成

- order: 2
  id: CM-03
  title: "2PC配信構成"
  rank: A
  rationale: >
    Phase 1-2 で構築した全ドメインの知識が統合される総合的なトピック。
    関心度が高く、Phase 3 の早い段階で公開する価値がある

- order: 3
  id: DO-05
  title: "Grafana監視"
  rank: B
  rationale: >
    Phase 2 の DO-03（VRAM Allocation）や Phase 1 の NE-01（配信停止の切り分け）
    と関連性が高い。ダッシュボードのビジュアルはサムネ映えし、
    DevOpsドメインの完結編として位置づけ

- order: 4
  id: AE-08
  title: "Dante / AoIP"
  rank: B
  rationale: >
    Phase 1-2 のオーディオシリーズの最終章。プロ向け機材前提で
    視聴者は限定的だが、差別化効果は最高。
    オーディオドメインの体系的コンテンツの完成

- order: 5
  id: CM-04
  title: "回線冗長化"
  rank: C
  rationale: >
    Phase 3 の CM-03（2PC配信構成）と合わせて、
    高可用性配信環境の構築を示す。予防系コンテンツだが、
    プロ志向の視聴者には価値が高い

- order: 6
  id: NE-05
  title: "WANボンディング"
  rank: C
  rationale: >
    Phase 1-2 のネットワークシリーズの完結編。
    CM-04（回線冗長化）と関連性が高く、セットで制作することで
    ネットワーク高可用性の体系的解説を完成させる

- order: 7
  id: DO-06
  title: "YouTube API自動化"
  rank: C
  rationale: >
    Phase 3 の締め。プログラマー向けでニッチだが、
    DO-04（Streamer.bot）と合わせて自動化シリーズを完結。
    Phase 1-3 全体の集大成として、技術的独自性を最大化
```

## 1.5. 全体の制作ロードマップ

<!--
これは全30本の推奨制作順序をまとめたものです。
全てを一度に制作する必要はありません。

現実的なペースの目安:
  - 個人制作で月1-2本程度が無理のないペース
  - Phase 1（10本）を半年程度で完了させることを目標にする
  - Phase 1 完了後、視聴者データを分析してから Phase 2 の順序を最終決定する
-->

### 1.5.1. 推奨制作順序の全体像

| 期間（目安） | Phase | 制作本数 | 目標 |
| --- | --- | --- | --- |
| 1-6ヶ月目 | Phase 1 | 11本 | 検索流入の確保とチャンネル方向性の確立 |
| 7-12ヶ月目 | Phase 2 前半 | 7本 | ドメイン別の体系的コンテンツ構築 |
| 13-18ヶ月目 | Phase 2 後半 | 6本 | 体系的コンテンツの完成 |
| 19ヶ月目以降 | Phase 3 | 7本 | 高度な自動化・カスタマイズ |

<!--
上記はあくまで目安です。制作ペースは個人の状況に合わせて調整してください。
重要なのは「中途半端に多くの動画を同時並行で作る」のではなく、
「1本を確実に完成させてから次に進む」ことです。
特に最初の3本は、チャンネルの品質基準を設定する重要な動画なので、
時間をかけて丁寧に仕上げることを推奨します。
Phase 1は11本とボリュームが大きいですが、全てが「検索流入獲得」を目指す
トラブルシューティング系コンテンツであり、チャンネルの基盤構築に不可欠です。
-->
