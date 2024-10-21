# modules/blockchain_loading.py
# Модуль для загрузки блокчейна

import os
import json
import hashlib  # Необходимо импортировать hashlib для хеширования

BLOCKCHAIN_DIR = "blockchains"

def load_blockchain(blockchain_name):
    """
    Загружает блокчейн по его имени.
    Возвращает данные блокчейна или None, если файл не найден.
    """
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
