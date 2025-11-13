"""
UE Development Agent - Warp風のローカルAIアシスタント
ファイル操作・コード生成・UEプロジェクト管理機能付き
"""
from langchain.llms import Ollama
from langchain.agents import Tool, AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
import os
import subprocess
from pathlib import Path

# ローカルモデル設定（Ollama使用）
llm = Ollama(
    model="my-ue-model",  # ファインチューニング後のモデル名
    temperature=0.1,
)

# ツール定義
def read_file(file_path: str) -> str:
    """ファイルの内容を読み込む"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"

def write_file(args: str) -> str:
    """ファイルに書き込む（形式: path|||content）"""
    try:
        path, content = args.split("|||", 1)
        with open(path.strip(), 'w', encoding='utf-8') as f:
            f.write(content.strip())
        return f"Successfully wrote to {path}"
    except Exception as e:
        return f"Error writing file: {e}"

def list_directory(path: str) -> str:
    """ディレクトリ内容を一覧表示"""
    try:
        items = os.listdir(path)
        return "\n".join(items)
    except Exception as e:
        return f"Error listing directory: {e}"

def search_files(args: str) -> str:
    """ファイル検索（形式: directory|||pattern）"""
    try:
        directory, pattern = args.split("|||", 1)
        matches = list(Path(directory.strip()).rglob(pattern.strip()))
        return "\n".join(str(m) for m in matches[:50])  # 最大50件
    except Exception as e:
        return f"Error searching files: {e}"

def analyze_ue_project(project_path: str) -> str:
    """UEプロジェクトの構造を分析"""
    try:
        uproject_files = list(Path(project_path).glob("*.uproject"))
        if not uproject_files:
            return "No .uproject file found"
        
        info = f"Project: {uproject_files[0].name}\n"
        
        # Source フォルダ確認
        source_dir = Path(project_path) / "Source"
        if source_dir.exists():
            cpp_files = list(source_dir.rglob("*.cpp"))
            h_files = list(source_dir.rglob("*.h"))
            info += f"C++ Files: {len(cpp_files)}\n"
            info += f"Header Files: {len(h_files)}\n"
        
        # Content フォルダ確認
        content_dir = Path(project_path) / "Content"
        if content_dir.exists():
            uasset_files = list(content_dir.rglob("*.uasset"))
            info += f"Assets: {len(uasset_files)}\n"
        
        return info
    except Exception as e:
        return f"Error analyzing project: {e}"

def run_ue_build(args: str) -> str:
    """UEプロジェクトのビルド（形式: project_path|||config）"""
    try:
        project_path, config = args.split("|||", 1)
        # UnrealBuildTool を呼び出す（パスは環境に合わせて調整）
        result = subprocess.run(
            ["UnrealBuildTool", "-projectfiles", project_path.strip()],
            capture_output=True,
            text=True,
            timeout=300
        )
        return result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        return f"Error building project: {e}"

# エージェントツール登録
tools = [
    Tool(
        name="ReadFile",
        func=read_file,
        description="Reads the contents of a file. Input: file path"
    ),
    Tool(
        name="WriteFile",
        func=write_file,
        description="Writes content to a file. Input format: 'path|||content'"
    ),
    Tool(
        name="ListDirectory",
        func=list_directory,
        description="Lists files and folders in a directory. Input: directory path"
    ),
    Tool(
        name="SearchFiles",
        func=search_files,
        description="Searches for files matching a pattern. Input format: 'directory|||pattern' (e.g., 'C:/Project|||*.cpp')"
    ),
    Tool(
        name="AnalyzeUEProject",
        func=analyze_ue_project,
        description="Analyzes an Unreal Engine project structure. Input: project root path"
    ),
    Tool(
        name="BuildUEProject",
        func=run_ue_build,
        description="Builds an Unreal Engine project. Input format: 'project_path|||config' (e.g., 'Development' or 'Shipping')"
    ),
]

# プロンプトテンプレート
template = """You are an expert Unreal Engine development assistant with access to file system tools.

You have access to the following tools:
{tools}

Tool Names: {tool_names}

Use this format:
Question: the input question
Thought: think about what to do
Action: the tool to use (must be one of [{tool_names}])
Action Input: the input to the tool
Observation: the result of the action
... (repeat Thought/Action/Observation as needed)
Thought: I now know the final answer
Final Answer: the final response to the user

Question: {input}

{agent_scratchpad}
"""

prompt = PromptTemplate.from_template(template)

# エージェント作成
agent = create_react_agent(llm, tools, prompt)
memory = ConversationBufferMemory(memory_key="chat_history")

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=True,
    max_iterations=10,
    handle_parsing_errors=True
)

# 使用例
if __name__ == "__main__":
    print("🎮 UE Development Agent - Ready!")
    print("Type 'exit' to quit\n")
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ['exit', 'quit']:
            break
        
        try:
            response = agent_executor.invoke({"input": user_input})
            print(f"\nAgent: {response['output']}\n")
        except Exception as e:
            print(f"Error: {e}\n")
