# modules/blockchain_listing.py
# Модуль для отображения списка блокчейнов
import os
import json
from rich.console import Console
from rich.table import Table

console = Console()
BLOCKCHAIN_DIR = "blockchains"

def list_blockchains():
    blockchains = []
    for filename in os.listdir(BLOCKCHAIN_DIR):
        if filename.endswith(".json"):
            blockchain_path = os.path.join(BLOCKCHAIN_DIR, filename)
            with open(blockchain_path, 'r') as f:
                blockchain_data = json.load(f)
                genesis_block = blockchain_data["blocks"][0]
                blockchain_name = genesis_block["data"]["blockchain_name"]
                owner = genesis_block["data"]["owner"]
                hash_genesis = genesis_block["hash"]
                blockchains.append((filename, blockchain_name, owner, hash_genesis))

    table = Table(title="Список блокчейнов")
    table.add_column("Имя файла")
    table.add_column("Имя блокчейна")
    table.add_column("Владелец")
    table.add_column("Хеш генезис-блока")

    for blockchain in blockchains:
        table.add_row(blockchain[0], blockchain[1], blockchain[2], blockchain[3])

    console.print(table)
