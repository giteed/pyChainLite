# modules/block_creation.py
# Модуль для создания нового блока в блокчейне

import hashlib
import json
import os
import time
from rich.console import Console

console = Console()

# Определяем путь к корневой директории
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOCKCHAIN_DIR = os.path.join(ROOT_DIR, "blockchains")

def create_new_block(blockchain_data, data, user_id):
    """
    Создает новый блок в блокчейне с указанными данными.
    """
    last_block = blockchain_data["blocks"][-1]
    previous_hash = last_block["hash"]

    new_block = {
        "index": last_block["index"] + 1,
        "timestamp": time.time(),
        "data": {
            "data": data,
            "added_by": user_id,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        },
        "previous_hash": previous_hash,
        "hash": ""
    }

    # Создаем хеш нового блока
    new_block_content = json.dumps(new_block, sort_keys=True).encode()
    new_block["hash"] = hashlib.sha256(new_block_content).hexdigest()

    # Добавляем новый блок в блокчейн
    blockchain_data["blocks"].append(new_block)

    # Получаем имя файла блокчейна для сохранения
    blockchain_name = blockchain_data["name"]
    blockchain_hash = hashlib.sha256(blockchain_name.encode()).hexdigest()
    blockchain_file = f"{blockchain_hash}.json"
    blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)

    console.print(f"[blue]Отладка:[/blue] Сохраняем блокчейн в файл: {blockchain_path}")

    # Сохраняем блокчейн обратно в файл
    with open(blockchain_path, 'w') as f:
        json.dump(blockchain_data, f, indent=4)

    return new_block
