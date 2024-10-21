# modules/blockchain_loading.py
import os
import json

BLOCKCHAIN_DIR = "blockchains"

def load_blockchain(blockchain_name):
    # Формируем имя файла на основе хеша блокчейна
    blockchain_hash = hashlib.sha256(blockchain_name.encode()).hexdigest()
    blockchain_file = f"{blockchain_hash}.json"
    blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)

    # Проверяем, существует ли файл блокчейна
    if not os.path.exists(blockchain_path):
        print(f"Ошибка: Блокчейн '{blockchain_name}' не найден.")
        return None

    # Загружаем блокчейн из файла
    with open(blockchain_path, 'r') as f:
        blockchain_data = json.load(f)

    return blockchain_data
