# EP012 / VT-04: Blend Shapes完全解説 - ARKit 52種パラメータの理解と最適化

## 必要な動画素材

### 画面キャプチャ

- ARKit Blend Shapesのパラメータ一覧画面（VTube Studio内の数値表示）
- VTube Studioのパラメータマッピング設定画面（入力パラメータ → Live2Dパラメータの対応付け）
- Live2D Cubism Editorのパラメータ設定画面（デフォーマとパラメータの紐付け）
- VTube Studioの表情テスト画面（各Blend Shapeを手動で操作するUI）

### デモ映像

- 52種類の主要Blend Shapesを一つずつ作動させたときの顔の変化デモ（以下を網羅）
  - 目: eyeBlinkLeft/Right, eyeWideLeft/Right, eyeSquintLeft/Right, eyeLookUp/Down/In/Out
  - 眉: browDownLeft/Right, browInnerUp, browOuterUpLeft/Right
  - 口: mouthOpen, mouthSmileLeft/Right, jawOpen, mouthPucker, mouthFunnel 等
  - 頬・鼻: cheekPuff, cheekSquintLeft/Right, noseSneerLeft/Right
  - 舌: tongueOut
- マッピングが不適切な状態のデモ（表情が過剰に動く / 表情が反応しない）
- マッピングを最適化した後のデモ（自然な表情変化）
- 複数のBlend Shapesが同時に作動する複合表情のデモ

### 図解・テロップ素材

- ARKit 52種Blend Shapesの全一覧表（名称 / 対応部位 / 動作説明）
- 顔面の3D図に各Blend Shape対応部位をマッピングした図
- VTube StudioとLive2Dのパラメータ対応関係図
- 推奨マッピング設定の早見表

## 必要機材

### 所有済み

- PC2: RTX 3060（VTube Studio動作用）
- iPhone（VT-03で購入済みの想定）
- Live2Dモデル: Beive / twintale（部分的なデモには使用可能）

### 追加購入（推奨）

- Full ARKit対応 Live2Dモデル（nizima等）: 10,000-50,000円
  - 本エピソードは52種のBlend Shapesを「一つずつ作動させた変化デモ」が必要
  - Beiveモデル: 紑20/52種カバー（統合入力）、個別デモ可能 0種。口周り21種、頬3種、齃2種が欠落
  - twintaleモデル: 紘18/52種カバー、個別デモ可能 1種（tongueOut）
  - 「ARKit 52 Blend Shapes対応」を明示しているモデルを選ぶこと
  - 代替案: VT-04の構成を変更し、VTube Studioのパラメータモニター（数値表示）と3D顔面図で解説する方式も可

### 購入時期

Phase 2。Phase 1制作中に判断すれば十分間に合う。
