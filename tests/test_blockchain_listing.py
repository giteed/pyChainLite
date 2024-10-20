# tests/test_blockchain_listing.py
import os
import json
from modules.blockchain_listing import list_blockchains

BLOCKCHAIN_DIR = "blockchains"

def test_list_blockchains(capsys):
    # Создаем тестовые блокчейны
    blockchain_names = ["blockchain1", "blockchain2"]
    for name in blockchain_names:
        blockchain_file = f"{hashlib.sha256(name.encode()).hexdigest()}.json"
        blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)
        
        blockchain_data = {
            "blocks": [{
                "index": 0,
                "data": {
                    "blockchain_name": name,
                    "owner": "owner_name"
                },
                "previous_hash": "0" * 64,
                "hash": hashlib.sha256("test_data".encode()).hexdigest()
            }]
        }
        os.makedirs(BLOCKCHAIN_DIR, exist_ok=True)
        with open(blockchain_path, 'w') as f:
            json.dump(blockchain_data, f, indent=4)

    # Тестируем вывод списка блокчейнов
    list_blockchains()
    captured = capsys.readouterr()
    for name in blockchain_names:
        assert name in captured.out

    # Удаляем созданные файлы после теста
    for name in blockchain_names:
        blockchain_file = f"{hashlib.sha256(name.encode()).hexdigest()}.json"
        os.remove(os.path.join(BLOCKCHAIN_DIR, blockchain_file))
