# tests/test_block_creation.py
import os
import json
import hashlib
from modules.block_creation import create_new_block

BLOCKCHAIN_DIR = "blockchains"

def test_create_new_block(monkeypatch):
    # Создаем тестовый блокчейн
    blockchain_name = "test_block_creation"
    blockchain_file = f"{hashlib.sha256(blockchain_name.encode()).hexdigest()}.json"
    blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)
    
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
    inputs = iter(["new block data"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Загружаем блокчейн и создаем новый блок
    create_new_block(blockchain_data)
    
    # Проверяем, что новый блок добавлен
    assert len(blockchain_data["blocks"]) == 2
    assert blockchain_data["blocks"][1]["data"] == "new block data"

    # Удаляем созданный файл после теста
    os.remove(blockchain_path)
