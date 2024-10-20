# tests/test_blockchain_loading.py
import os
import json
import hashlib
from modules.blockchain_loading import load_blockchain

BLOCKCHAIN_DIR = "blockchains"

def test_load_blockchain(monkeypatch):
    # Создаем тестовый блокчейн
    blockchain_name = "test_blockchain_loading"
    blockchain_hash = hashlib.sha256(blockchain_name.encode()).hexdigest()
    blockchain_file = f"{blockchain_hash}.json"
    blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)

    # Создаем тестовый генезис-блок
    blockchain_data = {
        "blocks": [{
            "index": 0,
            "data": {
                "blockchain_name": blockchain_name,
                "owner": "owner_name"
            },
            "previous_hash": "0" * 64,
            "hash": hashlib.sha256("test_data".encode()).hexdigest()
        }]
    }
    os.makedirs(BLOCKCHAIN_DIR, exist_ok=True)
    with open(blockchain_path, 'w') as f:
        json.dump(blockchain_data, f, indent=4)

    # Mock user inputs
    inputs = iter([blockchain_name])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    # Загружаем блокчейн
    blockchain = load_blockchain()
    assert blockchain["blocks"][0]["data"]["blockchain_name"] == blockchain_name

    # Удаляем созданный файл после теста
    os.remove(blockchain_path)
