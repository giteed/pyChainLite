# cli_scripts/push_data_in_block.py
# Скрипт для добавления данных в блок блокчейна через аргументы командной строки

import argparse
import os
import json
import sys
import hashlib  # Для хеширования имен блокчейнов
from datetime import datetime

# Добавляем путь к модулям в системный путь
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

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

    # Получаем номер последнего блока для определения номера нового блока
    last_block = blockchain_data["blocks"][-1]
    previous_hash = last_block["hash"]
    new_block_index = last_block["index"] + 1

    # Добавляем новый блок с переданными данными
    create_new_block(blockchain_data, data)

    # Сохраняем обновленный блокчейн
    with open(blockchain_path, 'w') as f:
        json.dump(blockchain_data, f, indent=4)
    
    # Формируем данные для вывода
    new_block_hash = blockchain_data["blocks"][-1]["hash"]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"Новый блок ({new_block_index}) с данными успешно добавлен в блокчейн '{blockchain_name}'.")
    print(f"Время добавления: {timestamp}")
    print(f"Хэш нового блока: {new_block_hash}")
    print(f"Хэш предыдущего блока: {previous_hash}")

if __name__ == "__main__":
    # Парсинг аргументов командной строки
    parser = argparse.ArgumentParser(description="Добавить данные в блок блокчейна")
    parser.add_argument("--blockchain-name", required=True, help="Имя блокчейна")
    parser.add_argument("--uid", required=True, help="Идентификатор пользователя для авторизации")
    parser.add_argument("data", help="Данные для добавления в новый блок")

    args = parser.parse_args()

    # Добавляем данные в блокчейн
    push_data_to_block(args.blockchain_name, args.uid, args.data)
