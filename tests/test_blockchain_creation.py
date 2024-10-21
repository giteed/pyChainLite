import os
import hashlib
import json
from modules.blockchain_creation import create_blockchain

BLOCKCHAIN_DIR = "blockchains"

def test_create_blockchain(monkeypatch):
    # Mock user inputs
    inputs = iter(["test_blockchain", "owner_name", "password123"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Создаем блокчейн
    blockchain_name = "test_blockchain"
    blockchain_hash = hashlib.sha256(blockchain_name.encode()).hexdigest()
    blockchain_file = f"{blockchain_hash}.json"
    blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)

    try:
        create_blockchain(blockchain_name, "owner_name")
        assert os.path.exists(blockchain_path)
    finally:
        # Удаляем созданный тестовый блокчейн
        if os.path.exists(blockchain_path):
            os.remove(blockchain_path)
