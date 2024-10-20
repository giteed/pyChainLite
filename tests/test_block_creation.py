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
        }],
        "file": blockchain_file  # Добавляем ключ "file" в данные блокчейна
    }

    # Создание папки для блокчейнов, если её нет
    os.makedirs(BLOCKCHAIN_DIR, exist_ok=True)

    # Сохраняем тестовый блокчейн в файл
    with open(blockchain_path, 'w') as f:
        json.dump(blockchain_data, f, indent=4)

    # Mock user inputs
    inputs = iter(["new block data"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Загружаем блокчейн и создаем новый блок
    new_block_data = "new block data"
    create_new_block(blockchain_data, new_block_data)

    # Проверка, что блок добавлен в блокчейн
    assert len(blockchain_data["blocks"]) == 2
    assert blockchain_data["blocks"][-1]["data"] == new_block_data
