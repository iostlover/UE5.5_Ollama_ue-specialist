# 🚀 UE5 Specialist - Ollama Model

A specialized Unreal Engine 5 AI model that runs locally. Generate UE5 C++ code, analyze projects, and edit files with AI assistance.

## ✨ Features

- **UE5 Specialized**: Trained on 28,703 UE5 C++ code samples
- **File Operations**: Read, create, and edit files directly
- **Code Generation**: Generate UE5 C++ code from natural language
- **Interactive Agent**: File manipulation with Warp-like functionality
- **Local Execution**: Runs completely offline - no internet required

## 📦 Installation (3 Steps)

### Step 1: Install Ollama

Download from https://ollama.ai and install for your OS.

```bash
ollama --version
```

### Step 2: Clone Repository

```bash
git clone https://github.com/yourusername/ue-specialist.git
cd ue-specialist
```

### Step 3: Setup Model

**In a new terminal:**

```bash
ollama serve
```

**In another terminal:**

```bash
ollama create ue-specialist -f models/Modelfile
```

Verify:

```bash
ollama list
# ue-specialist  latest  4.7gb
```

## 💻 Usage

### Method 1: Ollama Command Line

```bash
ollama run ue-specialist
>>> Create a PlayerController class that inherits from APlayerController
```

### Method 2: Python Agent (Recommended)

```bash
python agent/ue_agent.py

👤 You: read_file: C:\MyProject\Source\Character.h

👤 You: Implement a movement system using FVector in UE5

👤 You: write_file: C:\MyProject\Source\Movement.cpp | [AI-generated code]

👤 You: replace_in_file: C:\MyProject\Source\Character.cpp | old_code | new_code
```

## 📚 Documentation

- **[Agent Usage Guide](agent/UE_AGENT_README.md)** - Detailed instructions
- **[Command Reference](agent/FILE_EDITING_GUIDE.md)** - All available commands
- **[Project Information](docs/PROJECT_COMPLETE.md)** - Model development details

## 🎯 Available Commands

### File Operations

```bash
# View file contents
read_file: C:\path\to\file.cpp

# List directory contents
list_directory: C:\path\to\folder

# Create or edit file
write_file: C:\path\to\file.cpp | #include "CoreMinimal.h"

# Replace text in file
replace_in_file: C:\path\to\file.cpp | old_text | new_text
```

### Code Generation Examples

```
Implement this UE5 function
Add SetupPlayerInputComponent to PlayerController
Create a class that inherits from AActor and moves in Tick
```

## 📋 System Requirements

- Windows, macOS, or Linux
- Python 3.8+
- 8GB RAM minimum (16GB recommended)
- GPU recommended (NVIDIA/AMD), CPU works too
- 10GB disk space

## 🔧 Troubleshooting

### Ollama Connection Failed

```bash
ollama serve  # Start Ollama server
```

### Out of Memory

```bash
# Run on CPU only (slower)
ollama serve --num-gpu 0
```

### Model Not Found

```bash
ollama create ue-specialist -f models/Modelfile
```

### GPU Not Being Used

Update your GPU drivers:
- NVIDIA: https://www.nvidia.com/Download/driverDetails.aspx
- AMD: https://www.amd.com/en/support

## 📞 Support

If you encounter issues, please check [Issues](../../issues) or create a new one.

## 📝 License

MIT License

---

⭐ If this project helps you, please consider giving it a Star!
