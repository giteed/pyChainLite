# cli_scripts/push_data_in_block.py
# Скрипт для добавления данных в блок блокчейна через аргументы командной строки

import argparse
import os
import json
import hashlib  # Не забудьте импортировать hashlib для хеширования имен блокчейнов
from modules.blockchain_loading import load_blockchain
from modules.block_creation import create_new_block

BLOCKCHAIN_DIR = "blockchains"  # Путь к папке с блокчейнами

def push_data_to_block(blockchain_name, user_id, data):
    # Получаем хеш имени блокчейна на основе его имени
    blockchain_hash = hashlib.sha256(blockchain_name.encode()).hexdigest()
    blockchain_file = f"{blockchain_hash}.json"
    blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)

    # Проверяем, существует ли блокчейн
    if not os.path.exists(blockchain_path):
        print(f"Ошибка: Блокчейн '{blockchain_name}' не найден.")
        return

    # Загружаем блокчейн
    with open(blockchain_path, 'r') as f:
        blockchain_data = json.load(f)

    # Проверяем, есть ли у пользователя права на запись в блокчейн (простая проверка для примера)
    if user_id != blockchain_data["blocks"][0]["data"]["owner"]:
        print(f"Ошибка: Пользователь '{user_id}' не имеет прав на запись в этот блокчейн.")
        return

    # Добавляем новый блок с переданными данными
    create_new_block(blockchain_data, data)

    # Сохраняем обновленный блокчейн
    with open(blockchain_path, 'w') as f:
        json.dump(blockchain_data, f, indent=4)
    
    print(f"Данные успешно добавлены в блокчейн '{blockchain_name}'.")

if __name__ == "__main__":
    # Парсинг аргументов командной строки
    parser = argparse.ArgumentParser(description="Добавить данные в блок блокчейна")
    parser.add_argument("--blockchain-name", required=True, help="Имя блокчейна")
    parser.add_argument("--uid", required=True, help="Идентификатор пользователя для авторизации")
    parser.add_argument("data", help="Данные для добавления в новый блок")

    args = parser.parse_args()

    # Добавляем данные в блокчейн
    push_data_to_block(args.blockchain_name, args.uid, args.data)
