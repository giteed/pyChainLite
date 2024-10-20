# modules/block_creation.py
# Модуль для создания нового блока
import os
import json
from src.blockchain import Block
from rich.console import Console

console = Console()
BLOCKCHAIN_DIR = "blockchains"

def create_new_block(current_blockchain):
    if not current_blockchain:
        console.print("[red]Сначала загрузите блокчейн.[/red]")
        return

    data = input("Введите данные для нового блока: ").strip()
    last_block = current_blockchain["blocks"][-1]
    new_block = Block(
        index=last_block["index"] + 1,
        data=data,
        previous_hash=last_block["hash"]
    )

    current_blockchain["blocks"].append(new_block.__dict__)

    blockchain_path = os.path.join(BLOCKCHAIN_DIR, current_blockchain["file"])
    with open(blockchain_path, 'w') as f:
        json.dump(current_blockchain, f, indent=4)

    console.print(f"[green]Новый блок успешно добавлен в блокчейн.[/green]")
