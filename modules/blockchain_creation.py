# modules/blockchain_creation.py
# Модуль для создания блокчейна

import os
import json
import hashlib

BLOCKCHAIN_DIR = "blockchains"

def create_blockchain():
    """
    Создание нового блокчейна.
    """
    blockchain_name = input("Введите имя для нового блокчейна: ").strip()
    owner = input("Введите имя владельца: ").strip()
    owner_password = input("Введите пароль для владельца: ").strip()

    # Создание структуры блокчейна
    blockchain_data = {
        "blocks": [{
            "index": 0,
            "data": {
                "blockchain_name": blockchain_name,
                "owner": owner,
                "owner_password_hash": hashlib.sha256(owner_password.encode()).hexdigest()
            },
            "previous_hash": "0" * 64,
            "hash": hashlib.sha256(blockchain_name.encode()).hexdigest()
        }]
    }

    blockchain_file = f"{hashlib.sha256(blockchain_name.encode()).hexdigest()}.json"
    blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)

    os.makedirs(BLOCKCHAIN_DIR, exist_ok=True)

    # Сохранение блокчейна в файл
    with open(blockchain_path, 'w') as f:
        json.dump(blockchain_data, f, indent=4)

    print(f"Блокчейн '{blockchain_name}' успешно создан и сохранен.")
