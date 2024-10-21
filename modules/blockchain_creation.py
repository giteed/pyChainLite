# modules/blockchain_creation.py
# Модуль для создания нового блокчейна

import hashlib
import json
import os
from datetime import datetime
from rich.console import Console

console = Console()

# Путь к папке с блокчейнами
BLOCKCHAIN_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "blockchains")

def create_blockchain(blockchain_name, owner_name):
    """
    Создает новый блокчейн с указанным именем и владельцем.
    """
    # Проверяем наличие директории для хранения блокчейнов
    if not os.path.exists(BLOCKCHAIN_DIR):
        os.makedirs(BLOCKCHAIN_DIR)

    # Генерируем хеш для имени блокчейна
    blockchain_hash = hashlib.sha256(blockchain_name.encode()).hexdigest()
    blockchain_file = f"{blockchain_hash}.json"
    blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)

    # Проверяем, существует ли уже блокчейн с таким именем
    if os.path.exists(blockchain_path):
        console.print(f"[red]Ошибка: Блокчейн с именем '{blockchain_name}' уже существует.[/red]")
        return None

    # Генезис блок (первый блок)
    genesis_block = {
        "index": 0,
        "timestamp": datetime.now().isoformat(),
        "data": {
            "blockchain_name": blockchain_name,
            "owner": owner_name
        },
        "previous_hash": "0" * 64,
        "hash": ""
    }

    # Вычисляем хеш генезис-блока
    genesis_block_content = json.dumps(genesis_block, sort_keys=True).encode()
    genesis_block["hash"] = hashlib.sha256(genesis_block_content).hexdigest()

    # Создаем структуру блокчейна
    blockchain_data = {
        "name": blockchain_name,
        "blocks": [genesis_block]
    }

    # Сохраняем блокчейн в файл
    with open(blockchain_path, 'w') as f:
        json.dump(blockchain_data, f, indent=4)

    console.print(f"[green]Блокчейн '{blockchain_name}' успешно создан.[/green]")
    return blockchain_data
