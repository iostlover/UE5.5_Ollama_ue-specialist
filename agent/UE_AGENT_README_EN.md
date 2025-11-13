# 🤖 UE5 Agent - File Operations AI Assistant

An interactive AI agent powered by the ue-specialist Ollama model. Combines natural language AI with file system operations, similar to Warp's agentic capabilities.

## Overview

`ue_agent.py` provides:

1. **Natural Language Code Generation** - Generate UE5 C++ code from descriptions
2. **File Reading** - Review project source code
3. **File Creation & Editing** - Save AI-generated code to files
4. **Text Replacement** - Modify specific code sections

## System Requirements

- Ollama installed and running (`http://localhost:11434`)
- `ue-specialist` model registered in Ollama
- Python 3.8+
- Windows, macOS, or Linux

## Installation

```bash
# Install dependencies
pip install requests

# Start Ollama server
ollama serve
```

## Quick Start

```bash
python agent/ue_agent.py
```

You'll see:

```
======================================================================
🚀 UE5 Specialist - AI Agent (File Operations Support)
======================================================================

Usage:
  > read_file: C:\path\to\file.txt
  > list_directory: C:\path\to\folder
  > write_file: C:\path\to\file.txt | NEW CONTENT
  > replace_in_file: C:\path\to\file.txt | OLD TEXT | NEW TEXT
  > Any UE5 question or code request

Exit: exit or quit
```

## Commands

### 1. read_file - View File Contents

```bash
👤 You: read_file: C:\MyProject\Source\Character.h

🤖 Agent:
📄 File: C:\MyProject\Source\Character.h

#pragma once
#include "CoreMinimal.h"
#include "GameFramework/Character.h"
...
```

Shows first 1000 characters for large files.

### 2. list_directory - List Folder Contents

```bash
👤 You: list_directory: C:\MyProject\Source

🤖 Agent:
📁 Directory: C:\MyProject\Source

Total 5 items:

  📄 File: Character.cpp
  📄 File: Character.h
  📁 Folder: Public
  📁 Folder: Private
  📄 File: GameMode.h
```

### 3. write_file - Create or Update File

```bash
👤 You: write_file: C:\MyProject\Source\NewActor.h | #pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"

class MYPROJECT_API ANewActor : public AActor {
  GENERATED_BODY()
};

🤖 Agent:
✅ File created/updated: C:\MyProject\Source\NewActor.h (234 bytes)
```

**Features:**
- Auto-creates file if it doesn't exist
- Auto-creates parent directories
- Overwrites existing files

### 4. replace_in_file - Replace Text

```bash
👤 You: replace_in_file: C:\MyProject\Source\Character.cpp | void ACharacter::BeginPlay() { Super::BeginPlay(); } | void ACharacter::BeginPlay() { Super::BeginPlay(); UE_LOG(LogTemp, Warning, L"Spawned!"); }

🤖 Agent:
✅ File updated: C:\MyProject\Source\Character.cpp
Replacements: 1
```

**Notes:**
- Search string must match exactly
- Only first occurrence is replaced
- Multi-line: use `\n` for newlines

### 5. Natural Language - Ask AI to Generate Code

```bash
👤 You: Create a PlayerController class with SetupPlayerInputComponent implementation

🤖 UE5 Specialist:
Here's a PlayerController implementation:

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

## Practical Workflows

### Workflow 1: Create New Class from Scratch

```bash
# Step 1: Ask AI to generate code
👤 You: Create a FVector-based movement system. Include BeginPlay initialization and Tick updates.

# Step 2: Save header
👤 You: write_file: C:\MyProject\Source\MovementComponent.h | [AI header code]

# Step 3: Save implementation
👤 You: write_file: C:\MyProject\Source\MovementComponent.cpp | [AI cpp code]
```

### Workflow 2: Review and Fix Existing Code

```bash
# Step 1: View file
👤 You: read_file: C:\MyProject\Source\MyActor.cpp

# Step 2: Get AI feedback
👤 You: Check this code for potential memory leaks

# Step 3: Apply suggested fixes
👤 You: replace_in_file: C:\MyProject\Source\MyActor.cpp | delete pData; | if(pData) { delete pData; pData = nullptr; }
```

### Workflow 3: Edit JSON Configuration

```bash
# Step 1: Check current config
👤 You: read_file: C:\MyProject\Config\GameSettings.json

# Step 2: Update value
👤 You: replace_in_file: C:\MyProject\Config\GameSettings.json | "MaxPlayers": 4 | "MaxPlayers": 8
```

### Workflow 4: Generate Documentation

```bash
# Step 1: Ask for documentation
👤 You: Create markdown documentation explaining how to use the PlayerController class

# Step 2: Save it
👤 You: write_file: C:\MyProject\Docs\PlayerController_Guide.md | [AI-generated markdown]
```

## Advanced Usage

### Multi-line Replacements

Use `\n` for newlines:

```bash
👤 You: replace_in_file: C:\File.cpp | void MyFunc() {\n  return;\n} | void MyFunc() {\n  UE_LOG(LogTemp, Warning, L"Called");\n  return;\n}
```

### Large File Handling

`read_file` shows only first 1000 characters. For specific edits, use `replace_in_file` directly:

```bash
👤 You: replace_in_file: C:\LargeFile.cpp | EXACT_SEARCH_STRING | EXACT_REPLACEMENT
```

### Navigate Project Structure

```bash
👤 You: list_directory: C:\MyProject

👤 You: list_directory: C:\MyProject\Source

👤 You: list_directory: C:\MyProject\Source\Public
```

## Error Messages

| Error | Cause | Solution |
|-------|-------|----------|
| `❌ File not found` | Wrong path | Check path with `list_directory` |
| `❌ Search string not found` | Text doesn't match exactly | Use `read_file` to verify exact text |
| `❌ Cannot connect to Ollama` | Server not running | Run `ollama serve` |
| `❌ Model error` | Model not registered | Run `ollama create ue-specialist -f models/Modelfile` |

## Path Formats

Windows paths support both formats:

```bash
# Backslash (Windows standard)
read_file: C:\MyProject\Source\File.cpp

# Forward slash (Unix compatible)
read_file: C:/MyProject/Source/File.cpp
```

## Performance Tips

### Slow Responses

1. Check Ollama status
   ```bash
   ollama list
   ollama show ue-specialist
   ```

2. Keep prompts concise

3. Check GPU usage in Task Manager

### Insufficient Memory

- Switch to CPU-only mode: `ollama serve --num-gpu 0`
- Use lighter base model
- Reduce context length

## Exit

```bash
👤 You: exit

👋 Goodbye!
```

Or type `quit`.

## Troubleshooting

### Cannot connect to Ollama

```bash
# Verify server is running
ollama serve

# Test connection
curl http://localhost:11434/api/tags
```

### Model not found

```bash
# Check available models
ollama list

# Recreate model
ollama create ue-specialist -f models/Modelfile
```

### Python script won't run

```bash
# Check Python version
python --version

# If Python not found, use full path
C:\Users\YourName\AppData\Local\Programs\Python\Python311\python.exe agent/ue_agent.py
```

### File operations fail

1. Verify path exists
   ```bash
   list_directory: C:\MyProject
   ```

2. Check file is not read-only
   - Right-click file → Properties

3. Verify disk space available

## Configuration

Edit `agent/ue_agent.py` header to customize:

```python
MODEL_NAME = "ue-specialist"  # Model name
OLLAMA_API = "http://localhost:11434/api"  # API endpoint
```

## Security Notes

- **File Access**: This tool has direct filesystem access. Be careful with paths.
- **Backups**: Always backup important files before bulk edits
- **Code Review**: Review AI-generated code before using in production

## License

MIT License

## Related Documentation

- `FILE_EDITING_GUIDE.md` - Command reference
- `README.md` - Project overview
- `docs/PROJECT_COMPLETE.md` - Project details

---

**Version**: 1.0  
**Compatible Model**: ue-specialist (Ollama)
