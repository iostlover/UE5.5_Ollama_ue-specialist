#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
UE5 Specialist - ファイルアクセス対応 AI エージェント
Ollama モデル + ファイル操作機能
"""

import os
import sys
import requests
import json
from pathlib import Path

MODEL_NAME = "ue-specialist"
OLLAMA_API = "http://localhost:11434/api"

# ============================================================
# ツール定義
# ============================================================

def read_file(file_path: str) -> str:
    """ファイルの内容を読み込む"""
    try:
        path = Path(file_path)
        if not path.exists():
            return f"❌ ファイルが見つかりません: {file_path}"
        
        if path.is_dir():
            # フォルダの場合、内容を列挙
            files = list(path.iterdir())
            content = f"📁 フォルダ: {file_path}\n\n"
            content += "ファイル一覧:\n"
            for f in sorted(files):
                size = f.stat().st_size if f.is_file() else "-"
                ftype = "📄" if f.is_file() else "📁"
                content += f"  {ftype} {f.name} ({size} bytes)\n"
            return content
        else:
            # ファイルの場合、内容を読み込む
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 最初の1000文字のみ表示
            if len(content) > 1000:
                content = content[:1000] + "\n\n... (省略 - 最初の1000文字のみ表示)"
            
            return f"📄 ファイル: {file_path}\n\n{content}"
    
    except Exception as e:
        return f"❌ エラー: {e}"

def list_directory(dir_path: str) -> str:
    """ディレクトリの内容を一覧表示"""
    try:
        path = Path(dir_path)
        if not path.exists():
            return f"❌ ディレクトリが見つかりません: {dir_path}"
        
        if not path.is_dir():
            return f"❌ これはファイルです（ディレクトリではありません）: {dir_path}"
        
        files = list(path.iterdir())
        content = f"📁 ディレクトリ: {dir_path}\n\n"
        content += f"合計 {len(files)} 個のアイテム:\n\n"
        
        for f in sorted(files):
            size = f.stat().st_size if f.is_file() else "-"
            ftype = "📄 ファイル" if f.is_file() else "📁 フォルダ"
            content += f"  {ftype}: {f.name}\n"
        
        return content
    
    except Exception as e:
        return f"❌ エラー: {e}"

def write_file(file_path: str, content: str) -> str:
    """ファイルを作成または上書き"""
    try:
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"✅ ファイル作成/更新: {file_path} ({len(content)} bytes)"
    except Exception as e:
        return f"❌ エラー: {e}"

def replace_in_file(file_path: str, search: str, replace: str) -> str:
    """ファイル内の文字列を置換"""
    try:
        path = Path(file_path)
        if not path.exists():
            return f"❌ ファイルが見つかりません: {file_path}"
        
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if search not in content:
            return f"❌ 検索文字列が見つかりません: {search[:50]}..."
        
        new_content = content.replace(search, replace)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return f"✅ ファイル更新完了: {file_path}\n置換数: {new_content.count(replace) - content.count(replace)}"
    except Exception as e:
        return f"❌ エラー: {e}"

# ツール辞書
TOOLS = {
    "read_file": read_file,
    "list_directory": list_directory,
    "write_file": write_file,
    "replace_in_file": replace_in_file,
}

# ============================================================
# メイン
# ============================================================

def main():
    print("=" * 70)
    print("🚀 UE5 Specialist - AI エージェント（ファイルアクセス対応）")
    print("=" * 70)
    print()
    print("使用方法:")
    print('  > read_file: C:\\path\\to\\file.txt')
    print('  > list_directory: C:\\path\\to\\folder')
    print('  > write_file: C:\\path\\to\\file.txt | NEW CONTENT')
    print('  > replace_in_file: C:\\path\\to\\file.txt | OLD TEXT | NEW TEXT')
    print('  > UE5でActorをスポーン するコード')
    print()
    print("終了: exit または quit")
    print("=" * 70)
    print()
    
    while True:
        try:
            # ユーザー入力
            user_input = input("\n👤 あなた: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['exit', 'quit']:
                print("\n👋 さようなら！")
                break
            
            # ============================================================
            # ツール処理
            # ============================================================
            
            # read_file コマンド
            if user_input.startswith("read_file:"):
                file_path = user_input.replace("read_file:", "").strip()
                content = read_file(file_path)
                print(f"\n🤖 エージェント:\n{content}")
                continue
            
            # list_directory コマンド
            if user_input.startswith("list_directory:"):
                dir_path = user_input.replace("list_directory:", "").strip()
                content = list_directory(dir_path)
                print(f"\n🤖 エージェント:\n{content}")
                continue
            
            # write_file コマンド
            if user_input.startswith("write_file:"):
                parts = user_input.replace("write_file:", "").strip().split(" | ", 1)
                if len(parts) != 2:
                    print("❌ 形式: write_file: <path> | <content>")
                    continue
                file_path, content = parts
                result = write_file(file_path.strip(), content.strip())
                print(f"\n🤖 エージェント:\n{result}")
                continue
            
            # replace_in_file コマンド
            if user_input.startswith("replace_in_file:"):
                parts = user_input.replace("replace_in_file:", "").strip().split(" | ")
                if len(parts) != 3:
                    print("❌ 形式: replace_in_file: <path> | <search> | <replace>")
                    continue
                file_path, search, replace = parts
                result = replace_in_file(file_path.strip(), search.strip(), replace.strip())
                print(f"\n🤖 エージェント:\n{result}")
                continue
            
            # ============================================================
            # Ollama モデル処理
            # ============================================================
            
            print("\n⏳ 処理中...")
            
            try:
                response = requests.post(
                    f"{OLLAMA_API}/generate",
                    json={
                        "model": MODEL_NAME,
                        "prompt": user_input,
                        "stream": False
                    },
                    timeout=120
                )
                response.raise_for_status()
                
                result = response.json()
                output = result.get("response", "")
                
                print(f"\n🤖 UE5 Specialist:\n{output}")
                
                # 統計情報
                eval_count = result.get("eval_count", 0)
                eval_duration = result.get("eval_duration", 0)
                
                if eval_count > 0 and eval_duration > 0:
                    tokens_per_sec = eval_count / (eval_duration / 1e9)
                    print(f"\n📊 [{eval_count} tokens in {eval_duration/1e9:.2f}s = {tokens_per_sec:.1f} tokens/sec]")
            
            except requests.exceptions.Timeout:
                print("❌ タイムアウト（応答が長すぎる可能性があります）")
            except requests.exceptions.ConnectionError:
                print("❌ Ollama に接続できません（ollama serve を実行してください）")
            except Exception as e:
                print(f"❌ エラー: {e}")
        
        except KeyboardInterrupt:
            print("\n\n👋 中断しました")
            break
        except Exception as e:
            print(f"❌ エラー: {e}")

if __name__ == "__main__":
    main()
