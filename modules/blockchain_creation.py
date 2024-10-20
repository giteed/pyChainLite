# modules/blockchain_creation.py
# Скрипт для создания нового блокчейна

import hashlib
import json
import os
from datetime import datetime

# Путь к директории для хранения блокчейнов
BLOCKCHAIN_DIR = "blockchains"

def create_blockchain(blockchain_name, owner_name):
    """
    Функция для создания нового блокчейна с именем и владельцем.
    
    :param blockchain_name: Имя нового блокчейна
    :param owner_name: Имя владельца блокчейна
    :return: Данные нового блокчейна
    """
    # Хешируем имя блокчейна для создания имени файла
    blockchain_file = f"{hashlib.sha256(blockchain_name.encode()).hexdigest()}.json"
    blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)

    # Создаем папку для блокчейнов, если она не существует
    os.makedirs(BLOCKCHAIN_DIR, exist_ok=True)

    # Создаем генезис-блок
    genesis_block = {
        "index": 0,
        "timestamp": str(datetime.now()),
        "data": {
            "blockchain_name": blockchain_name,
            "owner": owner_name
        },
        "previous_hash": "0" * 64,
        "hash": hashlib.sha256(f"{blockchain_name}-{owner_name}".encode()).hexdigest()
    }

    # Создаем структуру блокчейна
    blockchain_data = {
        "blocks": [genesis_block],
        "file": blockchain_file
    }

    # Сохраняем блокчейн в файл
    with open(blockchain_path, 'w') as f:
        json.dump(blockchain_data, f, indent=4)

    print(f"Блокчейн '{blockchain_name}' успешно создан.")
    return blockchain_data
