# Github へのアップロード手順

既に Github リポジトリを作成してしまった場合の対応方法です。

## 📋 前提条件

- Git がインストールされている
- Github アカウントがある
- リポジトリが作成済み: `UE5.5_Ollama_ue-specialist`

## ⚠️ 注意：大容量ファイルについて

このプロジェクトに含まれるモデルファイルは 4-7 GB で非常に大きいため、以下の方法を推奨します：

### オプション A: Git LFS (Large File Storage) を使用 **【推奨】**

```bash
# 1. Git LFS をインストール
# Windows: https://git-lfs.github.com/ からインストーラーをダウンロード
# macOS: brew install git-lfs
# Linux: apt install git-lfs

# 2. Git LFS を初期化
git lfs install

# 3. 大容量ファイルをトラッキング
git lfs track "*.safetensors"
git lfs track "models/ue_model_gguf/**"

# 4. .gitattributes をコミット
git add .gitattributes
git commit -m "Add Git LFS configuration"
```

### オプション B: Github Releases を使用

大容量ファイルは Release として別途アップロードします（詳細は下記参照）

---

## 🚀 アップロード手順

### ステップ1: ローカルリポジトリを初期化

```bash
cd C:\OllamaModels\Github用

# Git を初期化（新しい場合）
git init

# または既存リポジトリから初期化
# git init --initial-branch=main
```

### ステップ2: 正しい README.md を設定

**以下の2つのファイルのうち、正しいものを README.md にリネーム:**

- `README_MAIN.md` → 統合版（英語+日本語）
- `README_EN.md` → 英語のみ
- `README.md` → 日本語のみ

**推奨: 統合版を使用**

```bash
# 統合版を README.md にリネーム
Copy-Item "README_MAIN.md" "README.md" -Force

# または削除して統合版を作成
Remove-Item "README.md" -Force
Copy-Item "README_MAIN.md" "README.md"
```

### ステップ3: Git にファイルを追加

```bash
# すべてのファイルをステージ
git add .

# または個別にステージ
git add README.md
git add .gitignore
git add agent/
git add models/Modelfile
git add models/Modelfile_base
git add docs/
```

**注意**: `models/ue_model_gguf/` のような大容量ファイルをスキップする場合:

```bash
# .gitignore に追加
echo "models/ue_model_gguf/" >> .gitignore
git add .gitignore
```

### ステップ4: 最初のコミット

```bash
git commit -m "Initial commit: UE5 Specialist Ollama model

- Complete ue-specialist model with file editing capabilities
- Python agent with natural language interface
- Documentation in English and Japanese
- Ready for global distribution"
```

### ステップ5: リモートを設定

```bash
# リモートを追加
git remote add origin https://github.com/yourusername/UE5.5_Ollama_ue-specialist.git

# ブランチ名確認
git branch -M main

# 確認
git remote -v
```

### ステップ6: アップロード

```bash
# プッシュ（初回）
git push -u origin main

# パスワードまたはトークンが求められたら入力
```

---

## 📦 大容量ファイルの処理

### オプション 1: Release でアップロード

Github リポジトリページで：

1. **Releases** をクリック
2. **Create a new release** をクリック
3. **Upload files** で `ue_model_gguf/` をアップロード
4. Release を公開

### オプション 2: Git LFS で管理

既に **ステップ3** で Git LFS を設定している場合、通常のコミットでOK。

---

## ✅ 確認

アップロード後、以下を確認してください：

```bash
# リモート状態確認
git remote -v

# ブランチ確認
git branch -a

# 最後のコミット確認
git log --oneline -n 3
```

---

## 🔄 既存リポジトリの上書き

### 方法1: Force Push（既存の README を上書き）

```bash
# ⚠️ 注意: 既存のコミットが失われます

git add .
git commit -m "Update: Replace with proper documentation"
git push -u origin main --force
```

### 方法2: 新しいリポジトリを作成

1. 古いリポジトリを削除
2. Github で新しいリポジトリを作成
3. 上記の手順でアップロード

---

## 🐛 トラブルシューティング

### エラー: "fatal: 'origin' does not appear to be a 'git' repository"

```bash
# リモートをリセット
git remote remove origin
git remote add origin https://github.com/yourusername/UE5.5_Ollama_ue-specialist.git
```

### エラー: "fatal: refusing to merge unrelated histories"

```bash
# 最初のプッシュが異なる履歴を持つ場合
git pull origin main --allow-unrelated-histories
git push origin main
```

### 大容量ファイルでアップロード失敗

```bash
# .gitignore で除外
echo "models/ue_model_gguf/" >> .gitignore
git add .gitignore
git commit -m "Exclude large model files from git"
git push origin main

# 別途 Release でアップロード
```

---

## 📝 最終チェックリスト

- ✅ README.md が正しく設定されている
- ✅ .gitignore が適切に設定されている
- ✅ agent/ フォルダがアップロードされている
- ✅ models/Modelfile がアップロードされている
- ✅ ドキュメント（.md ファイル）がアップロードされている
- ✅ models/ue_model_gguf/ が Git LFS または Release で管理されている

---

## 🎉 完了！

すべていけば、ユーザーは以下でクローンできます：

```bash
git clone https://github.com/yourusername/UE5.5_Ollama_ue-specialist.git
cd UE5.5_Ollama_ue-specialist
ollama serve
```

別ターミナルで：
```bash
ollama create ue-specialist -f models/Modelfile
python agent/ue_agent.py
```

---

**何か問題があれば、このガイドを参照してください！**
