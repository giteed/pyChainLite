# modules/block_creation.py
# Модуль для создания блоков и просмотра блоков в текущем блокчейне, включая поддержку данных через аргументы командной строки

import os
import json
from rich.console import Console
from src.blockchain import Block

console = Console()

BLOCKCHAIN_DIR = "blockchains"

def create_new_block(current_blockchain, data=None):
    """
    Создание нового блока в загруженном блокчейне.
    Аргумент `data` может быть передан извне или введен интерактивно.
    """
    if data is None:
        data = input("Введите данные для нового блока: ").strip()
    
    last_block = current_blockchain["blocks"][-1]
    new_block = Block(
        index=last_block["index"] + 1,
        data=data,
        previous_hash=last_block["hash"]
    )

    current_blockchain["blocks"].append(new_block.__dict__)

    blockchain_file = current_blockchain["file"]
    blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)
    
    # Сохраняем новый блок в файл блокчейна
    with open(blockchain_path, 'w') as f:
        json.dump(current_blockchain, f, indent=4)
    
    console.print(f"[green]Новый блок успешно добавлен в блокчейн {current_blockchain['blocks'][0]['data']['blockchain_name']}.[/green]")

def view_blocks(current_blockchain):
    """
    Просмотр всех блоков в загруженном блокчейне.
    """
    if not current_blockchain:
        console.print("[red]Блокчейн не загружен.[/red]")
        return

    console.print(f"Текущий блокчейн: [bold green]{current_blockchain['blocks'][0]['data']['blockchain_name']}[/bold green]\n")
    
    for block in current_blockchain["blocks"]:
        console.print(f"Block(index: {block['index']}, data: {block['data']}, hash: {block['hash']})")

