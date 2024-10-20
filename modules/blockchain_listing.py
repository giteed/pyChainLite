# modules/blockchain_listing.py
# Модуль для вывода списка блокчейнов

import os
import json
from rich.table import Table
from rich.console import Console

console = Console()

# Папка для хранения блокчейнов
BLOCKCHAIN_DIR = "blockchains"

def list_blockchains():
    if not os.path.exists(BLOCKCHAIN_DIR):
        console.print("[red]Папка с блокчейнами не найдена.[/red]")
        return

    blockchains = []
    for filename in os.listdir(BLOCKCHAIN_DIR):
        if filename.endswith(".json"):
            blockchain_path = os.path.join(BLOCKCHAIN_DIR, filename)
            file_size = os.path.getsize(blockchain_path)  # Получаем размер файла
            with open(blockchain_path, 'r') as f:
                blockchain_data = json.load(f)
                genesis_block = blockchain_data["blocks"][0]
                blockchain_name = genesis_block["data"]["blockchain_name"]
                owner = genesis_block["data"]["owner"]
                hash_genesis = genesis_block["hash"]
                block_count = len(blockchain_data["blocks"])  # Количество блоков
                blockchains.append((filename, block_count, file_size, blockchain_name, owner, hash_genesis))

    if not blockchains:
        console.print("[yellow]Нет созданных блокчейнов.[/yellow]")
        return

    # Таблица для вывода списка блокчейнов
    table = Table(title="Список блокчейнов", show_header=True, header_style="bold cyan")
    table.add_column("Имя файла", style="dim")
    table.add_column("Блоков", justify="center")
    table.add_column("Размер", justify="center")
    table.add_column("Имя блокчейна", style="bold")
    table.add_column("Владелец", style="bold")
    table.add_column("Хеш генезис-блока", style="bold")

    for blockchain in blockchains:
        table.add_row(
            blockchain[0], 
            str(blockchain[1]), 
            f"{blockchain[2] // 1024} KB",  # Размер в КБ
            blockchain[3], 
            blockchain[4], 
            blockchain[5]
        )

    console.print(table)
