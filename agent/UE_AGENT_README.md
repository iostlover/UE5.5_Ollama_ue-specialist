# 🤖 UE5 Agent - ファイル操作対応 AI エージェント

Ollama の `ue-specialist` モデルと連携し、Warp のようなファイルアクセス機能を備えた AI エージェント。

## 概要

`ue_agent.py` は以下の機能を提供します：

1. **自然言語でのコード生成** - UE5 C++ コード、JSON 設定、その他ファイルを生成
2. **ファイルの読み取り** - プロジェクトのコードを確認
3. **ファイルの作成・編集** - AI が生成したコードを直接ファイルに保存
4. **テキスト置換** - 既存ファイルの一部を修正

## システム要件

- **Ollama** がインストール・実行中（`http://localhost:11434`）
- `ue-specialist` モデルが Ollama に登録されていること
- Python 3.8 以上
- Windows/Mac/Linux

## インストール

```bash
# 依存パッケージのインストール
pip install requests pathlib

# Ollama の起動
ollama serve
```

## 使用方法

### 基本的な起動

```bash
python ue_agent.py
```

対話型プロンプトが起動します：

```
======================================================================
🚀 UE5 Specialist - AI エージェント（ファイルアクセス対応）
======================================================================

使用方法:
  > read_file: C:\path\to\file.txt
  > list_directory: C:\path\to\folder
  > write_file: C:\path\to\file.txt | NEW CONTENT
  > replace_in_file: C:\path\to\file.txt | OLD TEXT | NEW TEXT
  > UE5でActorをスポーン するコード

終了: exit または quit
```

### コマンド一覧

#### 1. **read_file** - ファイル内容の確認

```bash
👤 あなた: read_file: C:\MyProject\Source\Character.h

🤖 エージェント:
📄 ファイル: C:\MyProject\Source\Character.h

#pragma once
#include "CoreMinimal.h"
#include "GameFramework/Character.h"
...
```

ファイルが大きい場合は最初の 1000 文字を表示。

#### 2. **list_directory** - ディレクトリ一覧表示

```bash
👤 あなた: list_directory: C:\MyProject\Source

🤖 エージェント:
📁 ディレクトリ: C:\MyProject\Source

合計 5 個のアイテム:
  📄 ファイル: Character.cpp
  📄 ファイル: Character.h
  📁 フォルダ: Public
  📁 フォルダ: Private
  📄 ファイル: GameMode.h
```

#### 3. **write_file** - ファイル作成・上書き

```bash
👤 あなた: write_file: C:\MyProject\Source\NewActor.h | #pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"

class MYPROJECT_API ANewActor : public AActor {
  GENERATED_BODY()
};

🤖 エージェント:
✅ ファイル作成/更新: C:\MyProject\Source\NewActor.h (234 bytes)
```

**特徴:**
- ファイルが存在しなければ自動作成
- 親ディレクトリが存在しなければ自動作成
- 既存ファイルの場合は上書き

#### 4. **replace_in_file** - テキスト置換

```bash
👤 あなた: replace_in_file: C:\MyProject\Source\Character.cpp | void ACharacter::BeginPlay() { Super::BeginPlay(); } | void ACharacter::BeginPlay() { Super::BeginPlay(); UE_LOG(LogTemp, Warning, L"Character spawned!"); }

🤖 エージェント:
✅ ファイル更新完了: C:\MyProject\Source\Character.cpp
置換数: 1
```

**注意:**
- 検索文字列は完全一致である必要があります
- 複数マッチの場合は最初の 1 つのみ置換
- 複数行の置換は `\n` で改行を表現

#### 5. **通常の入力** - AI にコード生成を依頼

```bash
👤 あなた: UE5 で PlayerController を継承したクラスを作成してください。SetupPlayerInputComponent を実装してください。

🤖 UE5 Specialist:
以下のコードを参考にしてください：

#pragma once
#include "CoreMinimal.h"
#include "GameFramework/PlayerController.h"
#include "MyPlayerController.generated.h"

class MYPROJECT_API AMyPlayerController : public APlayerController {
    GENERATED_BODY()
    
public:
    virtual void SetupPlayerInputComponent(class UInputComponent* PlayerInputComponent) override;
};

...
```

## 実用的なワークフロー例

### 例1: 新しいクラスをゼロから作成

```bash
# ステップ1: AI にコード生成を依頼
👤 あなた: UE5 C++ で FVector を使う移動システムを実装してください。BeginPlay で初期化し、Tick で更新するコードをお願いします。

# ステップ2: AI がコードを生成したら、write_file でファイル保存
👤 あなた: write_file: C:\MyProject\Source\MovementComponent.h | [AIが生成したヘッダコード]

👤 あなた: write_file: C:\MyProject\Source\MovementComponent.cpp | [AIが生成したcppコード]
```

### 例2: 既存コードの確認・修正

```bash
# ステップ1: 既存ファイルを確認
👤 あなた: read_file: C:\MyProject\Source\MyActor.cpp

# ステップ2: AI にアドバイスをもらう
👤 あなた: このコードに メモリリークの可能性がないか確認してください

# ステップ3: AI の提案で置換
👤 あなた: replace_in_file: C:\MyProject\Source\MyActor.cpp | delete pData; | if(pData) { delete pData; pData = nullptr; }
```

### 例3: JSON 設定ファイルの編集

```bash
# ステップ1: 設定ファイルを確認
👤 あなた: read_file: C:\MyProject\Config\GameSettings.json

# ステップ2: 設定値を更新
👤 あなた: replace_in_file: C:\MyProject\Config\GameSettings.json | "MaxPlayers": 4 | "MaxPlayers": 8

# ステップ3: 別の設定も更新
👤 あなた: replace_in_file: C:\MyProject\Config\GameSettings.json | "Difficulty": "Normal" | "Difficulty": "Hard"
```

### 例4: ドキュメント生成

```bash
# AI にドキュメント生成を依頼
👤 あなた: このPlayerControllerクラスの使い方を説明するMarkdownファイルを作成してください

# AI がMarkdownを生成したら保存
👤 あなた: write_file: C:\MyProject\Docs\PlayerController_Guide.md | [AIが生成したMarkdown]
```

## 高度な使い方

### マルチラインテキストの置換

複数行のテキストを置換する場合は `\n` を使用：

```bash
👤 あなた: replace_in_file: C:\File.cpp | void MyFunc() {\n  return;\n} | void MyFunc() {\n  UE_LOG(LogTemp, Warning, L"Called");\n  return;\n}
```

### 大きなファイルの扱い

`read_file` は最初の 1000 文字のみ表示されます。特定部分の置換は `replace_in_file` で直接実行可能：

```bash
# 完全な内容を確認する必要がない場合は直接置換
👤 あなた: replace_in_file: C:\LargeFile.cpp | FIND_THIS_SPECIFIC_CODE | REPLACE_WITH_THIS
```

### ディレクトリ構造の確認

```bash
👤 あなた: list_directory: C:\MyProject

👤 あなた: list_directory: C:\MyProject\Source

👤 あなた: list_directory: C:\MyProject\Binaries
```

## エラーメッセージ

| エラー | 原因 | 対応 |
|--------|------|------|
| `❌ ファイルが見つかりません` | ファイルパスが正しくない | パスを確認（`read_file` で親ディレクトリを確認） |
| `❌ 検索文字列が見つかりません` | `replace_in_file` の検索文字列が存在しない | `read_file` でファイル内容を確認し、正確なテキストを指定 |
| `❌ Ollama に接続できません` | Ollama が実行されていない | `ollama serve` を実行 |
| `❌ [モデルエラー]` | モデルが登録されていない | `ollama pull ue-specialist` を実行 |

## パス形式について

Windows パスは両方のフォーマットに対応：

```bash
# バックスラッシュ（Windows標準）
read_file: C:\MyProject\Source\File.cpp

# スラッシュ（Unix互換）
read_file: C:/MyProject/Source/File.cpp
```

## パフォーマンス最適化

### 応答時間が遅い場合

1. **Ollama の設定を確認**
   ```bash
   ollama list
   ollama show ue-specialist
   ```

2. **コンテキスト長を短くする**
   - 入力プロンプトを簡潔に

3. **GPU の状態を確認**
   - タスクマネージャーで GPU 使用率を確認
   - 他の高負荷アプリケーションを終了

### メモリ不足エラー

- Ollama のモデルを軽量版に切り替え
- `ollama serve --num-gpu 0` で CPU のみで実行（遅い）

## 終了

```bash
👤 あなた: exit

👋 さようなら！
```

または

```bash
👤 あなた: quit
```

## トラブルシューティング

### Ollama に接続できない

```bash
# Ollama サーバーが起動しているか確認
ollama serve

# 別のターミナルでテスト
curl http://localhost:11434/api/tags
```

### ue-specialist モデルがない

```bash
# Ollama Hub から取得（個別で作成したモデルの場合は不要）
ollama pull ue-specialist

# または、事前に作成した Modelfile から生成
ollama create ue-specialist -f Modelfile
```

### ファイル操作がエラーになる

1. **パスが正しいか確認**
   ```bash
   list_directory: C:\MyProject
   ```

2. **ファイルが読み取り専用でないか確認**
   - ファイルを右クリック → プロパティで確認

3. **ディスク容量を確認**
   ```bash
   # Windows
   diskpart > list disk
   ```

### AI の応答がおかしい

- **プロンプトをより詳細に**
  ```bash
  👤 あなた: UE5.5 で AActor を継承し、BeginPlay で UE_LOG で "Hello" を出力するクラスを作成してください
  ```

- **モデルを再起動**
  ```bash
  ollama stop ue-specialist
  ollama serve
  ```

## 設定ファイル

`ue_agent.py` の先頭部分で設定可能：

```python
MODEL_NAME = "ue-specialist"  # 使用するモデル名
OLLAMA_API = "http://localhost:11434/api"  # Ollama API エンドポイント
```

## セキュリティに関する注意

- **ファイル操作**: ファイルシステムへの直接アクセスができます。危険なパスへのアクセスに注意
- **バックアップ**: 重要なファイルは事前にバックアップしておくことをお勧めします
- **出力の確認**: AI が生成したコードを実行前に確認してください

## ライセンス

MIT License

## 関連ドキュメント

- `FILE_EDITING_GUIDE.md` - 詳細な使用方法
- `README.md` - プロジェクト全体の説明
- `PROJECT_COMPLETE.md` - プロジェクト完成報告

---

**バージョン**: 1.0  
**対応モデル**: ue-specialist (Ollama)  
**更新日**: 2024年
