# push_data_in_block.py
# Скрипт для автоматической записи данных в блок с проверкой имени блокчейна и прав пользователя

import os
import json
import hashlib
import argparse
from rich.console import Console
from modules.blockchain_loading import load_blockchain
from modules.block_creation import create_new_block

console = Console()

# Путь к директории с блокчейнами
BLOCKCHAIN_DIR = "blockchains"

# Функция для хеширования имени блокчейна
def get_blockchain_hash(blockchain_name):
    return hashlib.sha256(blockchain_name.encode()).hexdigest()

# Функция для загрузки блокчейна по имени
def load_blockchain_by_name(blockchain_name):
    blockchain_hash = get_blockchain_hash(blockchain_name)
    blockchain_file = f"{blockchain_hash}.json"
    blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)

    if not os.path.exists(blockchain_path):
        console.print(f"[red]Ошибка: Блокчейн с именем '{blockchain_name}' не найден.[/red]")
        return None

    with open(blockchain_path, 'r') as f:
        blockchain_data = json.load(f)

    return blockchain_data

# Функция для проверки прав доступа (проверяет, есть ли user_id в списке разрешенных пользователей)
def check_user_permission(blockchain, user_id):
    genesis_block = blockchain["blocks"][0]
    owner = genesis_block["data"]["owner"]
    if user_id == owner:
        return True
    # Если требуется, можно расширить проверку прав (например, с дополнительными полями для разрешений)
    return False

def main():
    # Парсим аргументы командной строки
    parser = argparse.ArgumentParser(description="Добавить данные в блокчейн")
    parser.add_argument("--имя-блокчейна", required=True, help="Имя блокчейна, в который необходимо записать данные")
    parser.add_argument("--uid", required=True, help="User ID для проверки прав доступа")
    parser.add_argument("data", metavar="данные_для_записи", help="Данные, которые необходимо записать в блок")
    args = parser.parse_args()

    # Загрузка блокчейна по имени
    blockchain = load_blockchain_by_name(args.имя_блокчейна)
    if blockchain is None:
        return  # Блокчейн не найден, выходим

    # Проверка прав доступа
    if not check_user_permission(blockchain, args.uid):
        console.print(f"[red]Ошибка: У вас нет прав на запись в этот блокчейн.[/red]")
        return

    # Если права проверены, создаем новый блок
    create_new_block(blockchain, args.data)

    # Обновляем файл блокчейна с новым блоком
    blockchain_file = f"{get_blockchain_hash(args.имя_блокчейна)}.json"
    blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)
    with open(blockchain_path, 'w') as f:
        json.dump(blockchain, f, indent=4)

    console.print(f"[green]Новый блок успешно добавлен в блокчейн '{args.имя_блокчейна}'.[/green]")

if __name__ == "__main__":
    main()
