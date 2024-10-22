# tests/test_block_creation.py

import os
import json
import hashlib  # Импортируем hashlib
from modules.block_creation import create_new_block
from modules.blockchain_loading import BLOCKCHAIN_DIR

def test_create_new_block(monkeypatch):
    # Создаем тестовый блокчейн
    blockchain_name = "test_block_creation"
    blockchain_file = f"{hashlib.sha256(blockchain_name.encode()).hexdigest()}.json"  # Используем hashlib
    blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)

    blockchain_data = {
        "name": blockchain_name,  # Добавляем ключ 'name'
        "blocks": [{
            "index": 0,
            "data": {
                "blockchain_name": blockchain_name,
                "owner": "owner_name"
            },
            "previous_hash": "0" * 64,
            "hash": hashlib.sha256("test_data".encode()).hexdigest()  # Используем hashlib
        }],
        "file": blockchain_file
    }

    # Создание папки для блокчейнов, если её нет
    os.makedirs(BLOCKCHAIN_DIR, exist_ok=True)

    # Сохраняем тестовый блокчейн в файл
    with open(blockchain_path, 'w') as f:
        json.dump(blockchain_data, f, indent=4)

    # 🧪 Mock user inputs
    inputs = iter(["new block data"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Загружаем блокчейн и создаем новый блок
    new_block_data = "new block data"
    user_id = "test_user"  # Добавляем user_id
    create_new_block(blockchain_data, new_block_data, user_id=user_id)  # Передаем user_id

    # Проверяем, что новый блок был добавлен
    assert len(blockchain_data["blocks"]) == 2  # Новый блок добавлен
    assert blockchain_data["blocks"][-1]["data"]["data"] == new_block_data  # Данные совпадают
    assert blockchain_data["blocks"][-1]["data"]["added_by"] == user_id  # Проверка добавленного user_id
