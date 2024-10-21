# modules/blockchain_creation.py
import hashlib  # Импортируем hashlib
import json
import os
from datetime import datetime

BLOCKCHAIN_DIR = "blockchains"  # Путь к папке с блокчейнами

def create_blockchain(blockchain_name, owner_name):
    # Compute the hash-based filename
    blockchain_file = f"{hashlib.sha256(blockchain_name.encode()).hexdigest()}.json"
    blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)

    # Check if the blockchain already exists
    if os.path.exists(blockchain_path):
        print(f"[red]Блокчейн с именем '{blockchain_name}' уже существует.[/red]")
        overwrite = input("Вы хотите перезаписать существующий блокчейн? (y/n): ").strip().lower()
        if overwrite != 'y':
            return None

    # Proceed with the creation if confirmed
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

    # Write the blockchain to file
    with open(blockchain_path, 'w') as f:
        json.dump(blockchain_data, f, indent=4)
    
    return blockchain_data
