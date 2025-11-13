# 📝 UE5 Agent - File Editing Guide

Complete command reference and usage examples for the ue_agent.py file operations.

## Available Commands

### 1. read_file - Read File or Directory

```bash
read_file: C:\path\to\file.cpp
read_file: C:\path\to\folder
```

**Behavior:**
- File: Displays contents (first 1000 characters for large files)
- Folder: Lists all files and subfolders with sizes

**Examples:**
```bash
read_file: C:\UE5_Projects\MyGame\Source\MyCharacter.h

read_file: C:\UE5_Projects\MyGame\Source
```

### 2. list_directory - List Directory Contents

```bash
list_directory: C:\path\to\folder
```

**Behavior:** Displays all files and folders with icons and sizes

**Example:**
```bash
list_directory: C:\UE5_Projects\MyGame\Source

📁 Directory: C:\UE5_Projects\MyGame\Source

Total 5 items:

  📄 File: Character.cpp
  📄 File: Character.h
  📁 Folder: Public
  📁 Folder: Private
  📄 File: GameMode.h
```

### 3. write_file - Create or Overwrite File

```bash
write_file: C:\path\to\file.cpp | NEW CONTENT HERE
```

**Behavior:**
- Creates file if it doesn't exist
- Auto-creates parent directories if needed
- Overwrites existing file content
- Returns file path and size

**Examples:**
```bash
write_file: C:\UE5_Projects\MyGame\Source\NewActor.h | #pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"

class MYPROJECT_API ANewActor : public AActor {
  GENERATED_BODY()
};
```

**Output:**
```
✅ File created/updated: C:\UE5_Projects\MyGame\Source\NewActor.h (234 bytes)
```

### 4. replace_in_file - Replace Text in File

```bash
replace_in_file: C:\path\to\file.cpp | SEARCH_TEXT | REPLACEMENT_TEXT
```

**Behavior:**
- Finds first occurrence of SEARCH_TEXT
- Replaces with REPLACEMENT_TEXT
- File must already exist
- Returns number of replacements made

**Examples:**
```bash
replace_in_file: C:\MyGame\Source\Character.cpp | void BeginPlay() override { } | void BeginPlay() override { Super::BeginPlay(); UE_LOG(LogTemp, Warning, L"Game started!"); }
```

**Output:**
```
✅ File updated: C:\MyGame\Source\Character.cpp
Replacements: 1
```

## Usage Workflows

### Workflow 1: Generate and Save New Code

**Goal:** Create a new UE5 component class

```bash
# Step 1: Ask AI to generate code
👤 You: Generate a C++ component class that inherits from UActorComponent. 
         Include an OnBeginPlay method that logs a message.

# Step 2: AI generates the code
🤖 UE5 Specialist:
[Provides header and cpp code]

# Step 3: Save the header
👤 You: write_file: C:\MyProject\Source\Public\MyComponent.h | #pragma once

#include "CoreMinimal.h"
#include "Components/ActorComponent.h"
#include "MyComponent.generated.h"

UCLASS()
class MYPROJECT_API UMyComponent : public UActorComponent {
    GENERATED_BODY()

public:
    virtual void BeginPlay() override;
};

# Step 4: Save the implementation
👤 You: write_file: C:\MyProject\Source\Private\MyComponent.cpp | #include "MyComponent.h"

void UMyComponent::BeginPlay() {
    Super::BeginPlay();
    UE_LOG(LogTemp, Warning, L"MyComponent initialized!");
}
```

### Workflow 2: Review and Fix Existing Code

**Goal:** Review code and fix potential issues

```bash
# Step 1: Review the file
👤 You: read_file: C:\MyProject\Source\GameMode.cpp

# Step 2: Ask for feedback
👤 You: Check this code for potential memory leaks or issues

# Step 3: AI suggests improvements
🤖 UE5 Specialist: [Provides analysis and suggested fixes]

# Step 4: Apply fix
👤 You: replace_in_file: C:\MyProject\Source\GameMode.cpp | delete PlayerController; | if(PlayerController) { delete PlayerController; PlayerController = nullptr; }
```

### Workflow 3: Edit Configuration Files

**Goal:** Update game settings in JSON

```bash
# Step 1: View config
👤 You: read_file: C:\MyProject\Config\DefaultEngine.ini

# Step 2: Update multiple values
👤 You: replace_in_file: C:\MyProject\Config\DefaultEngine.ini | [/Script/Engine.GameSession] MaxPlayers=4 | [/Script/Engine.GameSession] MaxPlayers=8

# Step 3: Update another setting
👤 You: replace_in_file: C:\MyProject\Config\DefaultEngine.ini | bUseSplitscreen=False | bUseSplitscreen=True
```

### Workflow 4: Batch File Creation

**Goal:** Create multiple related files

```bash
# Create interface header
👤 You: write_file: C:\MyProject\Source\Public\DamageInterface.h | #pragma once

#include "CoreMinimal.h"
#include "UObject/Interface.h"
#include "DamageInterface.generated.h"

UINTERFACE(MinimalAPI, Blueprintable)
class UDamageInterface : public UInterface {
    GENERATED_BODY()
};

class IDamageInterface {
    GENERATED_BODY()

public:
    UFUNCTION(BlueprintNativeEvent, BlueprintCallable, Category = "Damage")
    float TakeDamage(float DamageAmount);
};

# Create implementation
👤 You: write_file: C:\MyProject\Source\Private\DamageInterface.cpp | #include "DamageInterface.h"

float IDamageInterface::Execute_TakeDamage_Implementation(UObject* Object, float DamageAmount) {
    return DamageAmount;
}
```

### Workflow 5: Generate and Save Documentation

**Goal:** Create API documentation

```bash
# Ask for documentation
👤 You: Create detailed markdown documentation for the PlayerController class. 
         Include usage examples, key methods, and best practices.

# AI generates comprehensive documentation
🤖 UE5 Specialist: [Provides full markdown]

# Save documentation
👤 You: write_file: C:\MyProject\Docs\PlayerController_API.md | # PlayerController API
[Complete documentation from AI]
```

## Advanced Techniques

### Multi-line Code Replacements

Use `\n` to represent newlines:

```bash
👤 You: replace_in_file: C:\File.cpp | void MyFunction() {\n    return;\n} | void MyFunction() {\n    UE_LOG(LogTemp, Warning, L"Function called");\n    return;\n}
```

### Path Variations

All these formats work:

```bash
# Windows backslash (standard)
read_file: C:\MyProject\Source\File.cpp

# Forward slash (Unix compatible)
read_file: C:/MyProject/Source/File.cpp

# Relative paths supported
read_file: MyProject/Source/File.cpp
```

### Large File Editing

For large files, use `replace_in_file` with specific, unique text:

```bash
# For large header files, use specific function signatures
👤 You: replace_in_file: C:\LargeHeaderFile.h | virtual void OnDeath() override; | virtual void OnDeath() override; UFUNCTION(BlueprintImplementableEvent) void DeathEvent();
```

### Directory Navigation

```bash
# List project root
👤 You: list_directory: C:\MyProject

# List source directory
👤 You: list_directory: C:\MyProject\Source

# List specific plugin
👤 You: list_directory: C:\MyProject\Plugins\MyPlugin\Source
```

## Error Handling

### File Not Found

```bash
❌ File not found: C:\MyProject\Source\NonExistent.h
```

**Solution:** Check path with `list_directory` first

### Search String Not Found

```bash
❌ Search string not found: void MyOldFunction()
```

**Solution:** Use `read_file` to verify exact text, including whitespace

### Directory Not Found

```bash
❌ Directory not found: C:\BadPath\
```

**Solution:** Use valid Windows path with correct case (Windows is case-insensitive but verify path exists)

### Permission Denied

```bash
❌ Error: Permission denied
```

**Solution:** 
- Check file is not read-only (Right-click → Properties)
- Ensure you have write permissions to directory
- Close file in other applications if locked

## Best Practices

### 1. Always Backup Important Files

Before running bulk replacements, backup your code:

```bash
# Verify backup
👤 You: read_file: C:\Backup\Character.cpp.backup
```

### 2. Use Specific Search Strings

Don't search for generic text:

```bash
# ❌ BAD - Too generic
replace_in_file: C:\File.cpp | void Init() { } | void Init() { Setup(); }

# ✅ GOOD - Specific to your code
replace_in_file: C:\File.cpp | void AMyCharacter::Init() { } | void AMyCharacter::Init() { Setup(); }
```

### 3. Test Replacements on Copies First

```bash
# Create test copy
👤 You: read_file: C:\MyProject\Source\Character.cpp
[Copy full contents]

👤 You: write_file: C:\MyProject\Source\Character_TEST.cpp | [Paste contents]

# Test replacement on copy
👤 You: replace_in_file: C:\MyProject\Source\Character_TEST.cpp | [search] | [replace]

# If successful, apply to original
👤 You: replace_in_file: C:\MyProject\Source\Character.cpp | [search] | [replace]
```

### 4. Use AI for Complex Replacements

Let AI help identify exact text:

```bash
👤 You: In the BeginPlay function of Character.cpp, show me the exact code I should replace 
        to add a damage system initialization.

# AI provides exact text to search for
🤖 UE5 Specialist: Here's the exact text to search for:
void AMyCharacter::BeginPlay() {
    Super::BeginPlay();
}

# Now you can replace it precisely
👤 You: replace_in_file: C:\MyProject\Source\Character.cpp | void AMyCharacter::BeginPlay() {\n    Super::BeginPlay();\n} | void AMyCharacter::BeginPlay() {\n    Super::BeginPlay();\n    InitializeDamageSystem();\n}
```

### 5. Organize Files Logically

```bash
# Check directory structure
👤 You: list_directory: C:\MyProject\Source\Public

# Create new files in correct location
👤 You: write_file: C:\MyProject\Source\Public\NewClass.h | [header content]

👤 You: write_file: C:\MyProject\Source\Private\NewClass.cpp | [implementation]
```

## File Size Limits

- **File Reading**: First 1000 characters displayed (use `replace_in_file` for large files)
- **File Writing**: No practical limit (tested with files >100MB)
- **Replacement**: Handles files up to available disk space

## Encoding

All files are handled in **UTF-8 encoding**. This supports:
- English and international characters
- Special symbols
- Code formatting (tabs, spaces, newlines)

## Tips & Tricks

### Quick Syntax Check

Ask AI to verify syntax before writing:

```bash
👤 You: Is this C++ code syntactically correct?
[Paste code]

🤖 UE5 Specialist: [Verifies syntax]

👤 You: write_file: C:\MyProject\Source\File.h | [code]
```

### Generate Multiple Files at Once

```bash
👤 You: Generate a complete actor class with header and implementation

# AI generates both
🤖 UE5 Specialist: 
Header:
[header content]

Implementation:
[cpp content]

# Save both
👤 You: write_file: C:\MyProject\Source\Public\Actor.h | [header]
👤 You: write_file: C:\MyProject\Source\Private\Actor.cpp | [impl]
```

### Version Control Integration

Track changes easily:

```bash
# Before editing
git add C:\MyProject\Source\Character.cpp

# Make edits with agent
👤 You: replace_in_file: C:\MyProject\Source\Character.cpp | old | new

# Check diff
git diff C:\MyProject\Source\Character.cpp
```

---

**Remember**: Always review AI-generated code and test thoroughly before production use!
