# Repository Structure Guide

## Directory Layout

```
ue-specialist-model/
├── README.md                          # Japanese introduction
├── README_EN.md                       # English introduction (START HERE for English users)
├── .gitignore                         # Git configuration
├── models/
│   ├── Modelfile                      # Main Ollama model configuration
│   ├── Modelfile_base                 # Base model settings
│   └── ue_model_gguf/
│       ├── ue_model_hf/               # Model weights & tokenizer
│       │   ├── config.json
│       │   ├── tokenizer.json
│       │   ├── special_tokens_map.json
│       │   └── checkpoint-**/         # Training checkpoints
│       └── Modelfile_HF               # HuggingFace model config
├── agent/
│   ├── ue_agent.py                    # Main agent script
│   ├── ue_dev_agent.py                # Developer variant
│   ├── UE_AGENT_README.md             # Japanese guide
│   ├── UE_AGENT_README_EN.md          # English guide
│   ├── FILE_EDITING_GUIDE.md          # Japanese command reference
│   └── FILE_EDITING_GUIDE_EN.md       # English command reference
└── docs/
    └── PROJECT_COMPLETE.md            # Project completion report
```

## File Descriptions

### Top-level
- **README.md** - Main documentation in Japanese with installation steps
- **README_EN.md** - Main documentation in English - recommended for English users
- **.gitignore** - Git configuration to exclude unnecessary files

### models/
- **Modelfile** - The main Ollama model configuration that users need
- **Modelfile_base** - Backup/alternative configuration
- **ue_model_gguf/ue_model_hf/** - The trained model weights and tokenizer files (large)

### agent/
- **ue_agent.py** - Main Python agent with file operations (run this)
- **ue_dev_agent.py** - Alternative agent implementation
- **UE_AGENT_README.md** - Detailed Japanese usage guide
- **UE_AGENT_README_EN.md** - Detailed English usage guide
- **FILE_EDITING_GUIDE.md** - Japanese command reference with examples
- **FILE_EDITING_GUIDE_EN.md** - English command reference with examples

### docs/
- **PROJECT_COMPLETE.md** - Information about model training and development

## Quick Start Guides

### For English Users
1. Read **README_EN.md**
2. Install Ollama from https://ollama.ai
3. Clone this repository
4. Run: `ollama serve` (in one terminal)
5. Run: `ollama create ue-specialist -f models/Modelfile` (in another terminal)
6. Run: `python agent/ue_agent.py` to start using it

### For Japanese Users
1. Read **README.md**
2. Ollama をインストール
3. リポジトリをクローン
4. `ollama serve` を実行
5. `ollama create ue-specialist -f models/Modelfile` を実行
6. `python agent/ue_agent.py` を実行

## File Selection

### Required Files
- Modelfile ✅ (must have)
- ue_model_gguf/ ✅ (the actual model)
- ue_agent.py ✅ (main script)
- Documentation ✅ (guides)

### Optional Files
- Modelfile_base (alternative)
- ue_dev_agent.py (alternative)
- PROJECT_COMPLETE.md (reference)

## Usage

```bash
# Clone the repository
git clone https://github.com/yourusername/ue-specialist.git
cd ue-specialist

# Start Ollama server (Terminal 1)
ollama serve

# Create the model (Terminal 2)
ollama create ue-specialist -f models/Modelfile

# Run the agent (Terminal 2)
python agent/ue_agent.py
```

## What This Model Does

- Generates UE5 C++ code
- Reads and analyzes files
- Creates new files
- Edits existing files
- Trained on 28,703 UE5 code samples

## Documentation

- **README.md** / **README_EN.md** - Start here
- **agent/UE_AGENT_README.md** / **UE_AGENT_README_EN.md** - Detailed usage
- **agent/FILE_EDITING_GUIDE.md** / **FILE_EDITING_GUIDE_EN.md** - Command reference

## Support

If you have issues:
1. Check the Troubleshooting section in README
2. Review the command guides
3. Open an Issue on GitHub

## License

MIT License - See LICENSE file

---

**Choose your language:**
- English: Start with [README_EN.md](README_EN.md)
- Japanese: Start with [README.md](README.md)
