# 🚀 UE5 Specialist - Ollama Model

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Ollama](https://img.shields.io/badge/Ollama-compatible-green.svg)](https://ollama.ai)

A specialized Unreal Engine 5 AI model for Ollama. Generate UE5 C++ code, analyze projects, and edit files with AI assistance.

Unreal Engine 5 特化型 Ollama AI モデル。UE5 C++ コード生成、プロジェクト分析、ファイル編集が可能。

## ✨ Features

- **UE5 Specialized**: Trained on 28,703 UE5 C++ code samples
- **File Operations**: Read, create, and edit files directly  
- **Code Generation**: Generate UE5 C++ code from natural language
- **Interactive Agent**: File manipulation with AI assistance
- **Local Execution**: Runs completely offline - no internet required

## 📋 System Requirements

- Windows, macOS, or Linux
- Python 3.8+
- 8GB RAM minimum (16GB recommended)
- GPU recommended (NVIDIA/AMD), CPU works too
- 10GB disk space

## 🚀 Quick Start (3 Steps)

### Step 1: Install Ollama

Download from https://ollama.ai

```bash
ollama --version
```

### Step 2: Clone Repository

```bash
git clone https://github.com/yourusername/UE5.5_Ollama_ue-specialist.git
cd UE5.5_Ollama_ue-specialist
```

### Step 3: Setup & Run

**Terminal 1:**
```bash
ollama serve
```

**Terminal 2:**
```bash
ollama create ue-specialist -f models/Modelfile
python agent/ue_agent.py
```

## 💻 Usage Examples

### Generate Code
```bash
👤 You: Create a PlayerController class with SetupPlayerInputComponent

🤖 UE5 Specialist: [Generates UE5 C++ code]
```

### Edit Files
```bash
👤 You: read_file: C:\MyProject\Source\Character.h

👤 You: write_file: C:\MyProject\Source\NewActor.cpp | [code]

👤 You: replace_in_file: C:\MyProject\Source\Character.cpp | old | new
```

## 📚 Documentation

### English
- **[README_EN.md](README_EN.md)** - Full English guide
- **[agent/UE_AGENT_README_EN.md](agent/UE_AGENT_README_EN.md)** - Agent usage (English)
- **[agent/FILE_EDITING_GUIDE_EN.md](agent/FILE_EDITING_GUIDE_EN.md)** - Command reference (English)

### 日本語
- **[README.md](README.md)** - 完全な日本語ガイド
- **[agent/UE_AGENT_README.md](agent/UE_AGENT_README.md)** - エージェント使用方法
- **[agent/FILE_EDITING_GUIDE.md](agent/FILE_EDITING_GUIDE.md)** - コマンドリファレンス

## 🎯 Available Commands

```bash
# Read file or directory
read_file: C:\path\to\file.cpp

# List folder contents
list_directory: C:\path\to\folder

# Create or edit file
write_file: C:\path\to\file.cpp | #include "CoreMinimal.h"

# Replace text
replace_in_file: C:\path\to\file.cpp | old_text | new_text
```

## 🔧 Troubleshooting

### Cannot connect to Ollama
```bash
ollama serve
```

### Out of Memory
```bash
ollama serve --num-gpu 0  # CPU only
```

### Model not found
```bash
ollama create ue-specialist -f models/Modelfile
```

## 📦 What's Included

- ✅ `ue-specialist` model (4.7 GB)
- ✅ Python agent with file operations
- ✅ Complete documentation (English & Japanese)
- ✅ Examples and workflows

## 📊 Model Information

| Item | Details |
|------|---------|
| **Base Model** | Qwen2.5-Coder-7B |
| **Training Data** | 28,703 UE5 C++ samples + documentation |
| **Method** | QLoRA (4-bit quantization) |
| **Format** | GGUF (Ollama compatible) |
| **Size** | 4-7 GB |
| **Environment** | NVIDIA GPU 6GB+ or CPU |

## 📝 License

MIT License - See LICENSE file

## 🤝 Support

- 📖 Check documentation first
- 🐛 Found a bug? [Open an Issue](../../issues)
- 💬 Have questions? [Discussions](../../discussions)

## 🙏 Acknowledgments

- [Ollama](https://ollama.ai) - Local LLM runtime
- [Unsloth](https://github.com/unslothai/unsloth) - Fast fine-tuning
- [Qwen Team](https://github.com/QwenLM) - Base model

---

**Choose your language:**
- 🌐 [English Guide](README_EN.md)
- 🇯🇵 [日本語ガイド](README.md)

⭐ If this helps you, please consider giving it a Star!
