# tests/test_blockchain_creation.py
import hashlib
import os
import json
from modules.blockchain_creation import create_blockchain
from modules.blockchain_loading import BLOCKCHAIN_DIR

def test_create_blockchain(monkeypatch):
    # Mock user inputs
    inputs = iter(["test_blockchain", "owner_name", "password123"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Создаем блокчейн (передаем необходимые аргументы)
    blockchain_name = "test_blockchain"
    owner_name = "owner_name"
    created_blockchain = create_blockchain(blockchain_name, owner_name)
    
    # Проверяем, что блокчейн создан
    assert created_blockchain["name"] == blockchain_name
    assert created_blockchain["blocks"][0]["data"]["owner"] == owner_name
