# modules/blockchain_creation.py
import hashlib
import json
import os
from datetime import datetime

BLOCKCHAIN_DIR = "blockchains"

def create_blockchain(blockchain_name, owner_name):
    # Генерируем имя файла для блокчейна на основе хеша
    blockchain_file = f"{hashlib.sha256(blockchain_name.encode()).hexdigest()}.json"
    blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)

    # Проверка: если файл блокчейна уже существует
    if os.path.exists(blockchain_path):
        print(f"[red]Блокчейн с именем '{blockchain_name}' уже существует.[/red]")
        return None  # Прерываем создание блокчейна

    # Данные для нового блокчейна
    blockchain_data = {
        "name": blockchain_name,
        "blocks": [{
            "index": 0,
            "timestamp": get_current_time(),
            "data": {
                "blockchain_name": blockchain_name,
                "owner": owner_name
            },
            "previous_hash": "0" * 64,
            "hash": hashlib.sha256("genesis".encode()).hexdigest()
        }]
    }

    # Сохраняем блокчейн в файл
    with open(blockchain_path, 'w') as f:
        json.dump(blockchain_data, f, indent=4)

    return blockchain_data

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
