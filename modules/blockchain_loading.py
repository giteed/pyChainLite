# blockchain_loading.py
# Модуль для загрузки блокчейна по его имени

import os
import json

BLOCKCHAIN_DIR = "blockchains"

def load_blockchain(blockchain_name):
    """
    Загружает блокчейн по имени.
    
    :param blockchain_name: Имя блокчейна для загрузки
    :return: Данные блокчейна или None, если файл не найден
    """
    # Хешируем имя блокчейна для нахождения файла
    blockchain_file = f"{blockchain_name}.json"
    blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)

    # Проверяем, существует ли файл блокчейна
    if os.path.exists(blockchain_path):
        with open(blockchain_path, 'r') as f:
            blockchain_data = json.load(f)
        print(f"Блокчейн '{blockchain_name}' успешно загружен.")
        return blockchain_data
    else:
        print(f"Ошибка: Блокчейн '{blockchain_name}' не найден.")
        return None
