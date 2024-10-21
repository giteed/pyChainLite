# tests/test_blockchain_loading.py
import hashlib
import os
import json
from modules.blockchain_loading import load_blockchain, BLOCKCHAIN_DIR

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

    # Создание директории для блокчейнов
    os.makedirs(BLOCKCHAIN_DIR, exist_ok=True)

    # Сохраняем блокчейн в файл
    with open(blockchain_path, 'w') as f:
        json.dump(blockchain_data, f, indent=4)

    # Mock user inputs
    inputs = iter([blockchain_name])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Загружаем блокчейн (передаем аргумент blockchain_name)
    blockchain = load_blockchain(blockchain_name)

    # Проверяем, что блокчейн успешно загружен
    assert blockchain is not None, f"Ошибка: Блокчейн '{blockchain_name}' не был загружен."
    assert blockchain["blocks"][0]["data"]["blockchain_name"] == blockchain_name
