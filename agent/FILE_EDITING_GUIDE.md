# 📝 UE5 Agent - ファイル編集機能ガイド

## 概要
`ue_agent.py` には、Ollama の UE5 Specialist モデルと連携してファイルの読み書きができる機能があります。Warp のようにファイルアクセスと AI の力を組み合わせることができます。

## 利用可能なコマンド

### 1. **read_file** - ファイル/フォルダの内容を読む

```bash
read_file: C:\path\to\file.cpp
read_file: C:\path\to\folder
```

**動作**:
- ファイルを指定: ファイルの内容を表示（最初の1000文字）
- フォルダを指定: フォルダ内のファイル一覧を表示

**例**:
```bash
read_file: C:\UE5_Projects\MyGame\Source\MyCharacter.h
```

### 2. **list_directory** - ディレクトリを詳細表示

```bash
list_directory: C:\path\to\folder
```

**動作**: フォルダ内のすべてのファイル/サブフォルダをリスト表示

**例**:
```bash
list_directory: C:\UE5_Projects\MyGame\Source
```

### 3. **write_file** - ファイルを作成または上書き

```bash
write_file: C:\path\to\file.cpp | NEW CONTENT HERE
```

**動作**:
- ファイルが存在しない場合: 新しいファイルを作成
- ファイルが存在する場合: 内容を上書き
- 親ディレクトリが存在しない場合: 自動作成

**例**:
```bash
write_file: C:\UE5_Projects\MyGame\Source\NewActor.cpp | #include "MyActor.h"
void AMyActor::BeginPlay() {
    Super::BeginPlay();
}
```

### 4. **replace_in_file** - ファイル内のテキストを置換

```bash
replace_in_file: C:\path\to\file.cpp | OLD TEXT | NEW TEXT
```

**動作**: 最初にマッチしたテキストを置換

**例**:
```bash
replace_in_file: C:\UE5_Projects\MyGame\Source\Character.cpp | void OnDeath() { } | void OnDeath() { Destroy(); }
```

## 使用ワークフロー例

### シナリオ1: 既存コードの確認と修正

```bash
# 1. ファイルの内容を確認
read_file: C:\MyProject\Source\Actor.cpp

# 2. AI に修正を依頼（通常の入力）
このActorクラスのBeginPlay関数を修正して、スポーン時にログを出力するようにしてください

# 3. AI が提案したコードで置換
replace_in_file: C:\MyProject\Source\Actor.cpp | void AMyActor::BeginPlay() { Super::BeginPlay(); } | void AMyActor::BeginPlay() { Super::BeginPlay(); UE_LOG(LogTemp, Warning, L"Actor spawned!"); }
```

### シナリオ2: 新しいファイルを作成

```bash
# AI にコードを生成させる
UE5 C++ で PlayerController を継承した MyPlayerController クラスを作成してください

# AI が生成したコードをファイルに保存
write_file: C:\MyProject\Source\MyPlayerController.h | [AIが生成したコード]

write_file: C:\MyProject\Source\MyPlayerController.cpp | [AIが生成したコード]
```

### シナリオ3: JSON 設定ファイルの編集

```bash
# 設定ファイルを確認
read_file: C:\MyProject\Config\GameConfig.json

# 設定値を更新
replace_in_file: C:\MyProject\Config\GameConfig.json | "MaxPlayers": 4 | "MaxPlayers": 8
```

## 高度な使い方

### マルチラインコンテンツの書き込み

複数行のコンテンツを書き込む場合は、改行文字 `\n` を使用します:

```bash
write_file: C:\MyProject\Source\MyClass.h | #pragma once\n\nclass AMyClass {\npublic:\n  void MyFunction();\n};
```

### 大きなファイルの処理

ファイルが大きい場合、`read_file` は最初の1000文字のみ表示されます。

該当部分を特定した後に `replace_in_file` で置換してください:

```bash
# ファイルの最初の部分を確認
read_file: C:\LargeFile.cpp

# 置換対象を明確に指定
replace_in_file: C:\LargeFile.cpp | SPECIFIC_OLD_CODE | NEW_CODE
```

## AI と連携した典型的なフロー

1. **質問**: コマンドラインで自然言語で質問
   ```bash
   UE5 で FVector を使ったキャラクターの移動システムを実装してください
   ```

2. **AI からの提案**: AI がコード例を生成

3. **ファイル保存**: `write_file` コマンドで生成されたコードを保存
   ```bash
   write_file: C:\Project\Source\Movement.cpp | [生成されたコード]
   ```

4. **既存コードの修正**: `replace_in_file` で部分的に修正
   ```bash
   replace_in_file: C:\Project\Source\Movement.cpp | old_function() | new_function()
   ```

## エラーハンドリング

- **ファイルが見つからない**: `❌ ファイルが見つかりません: [パス]`
- **置換対象が見つからない**: `❌ 検索文字列が見つかりません: [検索文字列]`
- **パスが無効**: `❌ エラー: [エラー詳細]`

## ヒント

- **パスの形式**: Windows パスは `C:\path\to\file` または `C:/path/to/file` の両方に対応
- **エンコード**: UTF-8 で自動処理されます
- **バックアップ**: 大切なファイルは事前にバックアップしてください
- **置換の確認**: 複数行の置換は `replace_in_file` で一度に 1 つずつ実行することをお勧めします

## 終了方法

```bash
exit
# または
quit
```

---

**作成日**: 2024年
**バージョン**: 1.0
**対応モデル**: ue-specialist (Ollama)
