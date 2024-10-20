# tests/test_blockchain_creation.py
import os
import json
import hashlib
from modules.blockchain_creation import create_blockchain

BLOCKCHAIN_DIR = "blockchains"

def test_create_blockchain(monkeypatch):
    # Mock user inputs
    inputs = iter(["test_blockchain", "owner_name", "password123"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    # Создаем блокчейн
    create_blockchain()
    
    # Проверяем, что файл блокчейна создан
    blockchain_hash = hashlib.sha256("test_blockchain".encode()).hexdigest()
    blockchain_file = f"{blockchain_hash}.json"
    blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)

    assert os.path.exists(blockchain_path), "Файл блокчейна не создан"

    # Проверяем содержимое блокчейна
    with open(blockchain_path, 'r') as f:
        blockchain_data = json.load(f)
    
    genesis_block = blockchain_data["blocks"][0]
    assert genesis_block["data"]["blockchain_name"] == "test_blockchain"
    assert genesis_block["data"]["owner"] == "owner_name"

    # Удаляем созданный файл после теста
    os.remove(blockchain_path)
