# modules/blockchain_creation.py
import hashlib
import json
import os
from datetime import datetime

BLOCKCHAIN_DIR = "blockchains"

def blockchain_exists(blockchain_name):
    """
    Проверяет, существует ли блокчейн с данным именем.
    """
    blockchain_file = f"{hashlib.sha256(blockchain_name.encode()).hexdigest()}.json"
    blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)
    return os.path.exists(blockchain_path)

def create_blockchain(blockchain_name, owner_name):
    """
    Создает новый блокчейн.
    """
    if blockchain_exists(blockchain_name):
        return None

    blockchain_file = f"{hashlib.sha256(blockchain_name.encode()).hexdigest()}.json"
    blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)

    os.makedirs(BLOCKCHAIN_DIR, exist_ok=True)

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

    blockchain_data = {
        "name": blockchain_name,
        "blocks": [genesis_block],
        "file": blockchain_file
    }

    with open(blockchain_path, 'w') as f:
        json.dump(blockchain_data, f, indent=4)

    print(f"Блокчейн '{blockchain_name}' успешно создан.")
    return blockchain_data
