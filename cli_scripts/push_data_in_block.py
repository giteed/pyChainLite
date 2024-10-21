# cli_scripts/push_data_in_block.py
# Скрипт для добавления данных в блок блокчейна через аргументы командной строки
# Пример использования:
# python3 push_data_in_block.py --blockchain-name alfa --uid edd "cli test add data to block"

import argparse
import os
import json
import sys
import hashlib
from datetime import datetime
from rich.console import Console

# Добавляем путь к модулям в системный путь
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from modules.blockchain_loading import load_blockchain
from modules.block_creation import create_new_block

BLOCKCHAIN_DIR = "blockchains"  # Путь к папке с блокчейнами

console = Console()

def push_data_to_block(blockchain_name, user_id, data):
    """
    Добавляет новый блок с данными в существующий блокчейн.
    """
    console.print(f"[blue]Отладка:[/blue] Имя блокчейна: {blockchain_name}")
    console.print(f"[blue]Отладка:[/blue] Идентификатор пользователя: {user_id}")
    console.print(f"[blue]Отладка:[/blue] Данные: {data}")

    # Проверка на наличие данных
    if not data.strip():
        console.print("[red]Ошибка: Нельзя добавить блок с пустыми данными![/red]")
        return

    # Получаем хеш имени блокчейна на основе его имени
    blockchain_hash = hashlib.sha256(blockchain_name.encode()).hexdigest()
    console.print(f"[blue]Отладка:[/blue] Хэш блокчейна: {blockchain_hash}")

    blockchain_file = f"{blockchain_hash}.json"
    blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)
    console.print(f"[blue]Отладка:[/blue] Путь к файлу блокчейна: {blockchain_path}")

    # Проверяем, существует ли блокчейн
    if not os.path.exists(blockchain_path):
        console.print(f"[red]Ошибка: Блокчейн '{blockchain_name}' не найден по пути: {blockchain_path}[/red]")
        return

    # Загружаем блокчейн
    console.print("[blue]Отладка:[/blue] Загружаем блокчейн...")
    blockchain_data = load_blockchain(blockchain_name)

    if blockchain_data is None:
        console.print(f"[red]Ошибка: Не удалось загрузить данные блокчейна '{blockchain_name}'.[/red]")
        return

    console.print(f"[blue]Отладка:[/blue] Блокчейн успешно загружен: {blockchain_data}")

    # Проверяем, есть ли у пользователя права на запись в блокчейн
    if user_id != blockchain_data["blocks"][0]["data"]["owner"]:
        console.print(f"[red]Ошибка: Пользователь '{user_id}' не имеет прав на запись в этот блокчейн.[/red]")
        return

    # Добавляем новый блок с переданными данными
    new_block = create_new_block(blockchain_data, data, user_id=user_id)

    # Преобразуем timestamp в читаемый формат
    readable_time = datetime.fromtimestamp(float(new_block["timestamp"])).strftime('%Y-%m-%d %H:%M:%S')

    # Сохраняем обновленный блокчейн
    with open(blockchain_path, 'w') as f:
        json.dump(blockchain_data, f, indent=4)
    
    # Выводим информацию о новом блоке
    console.print(f"[green]Новый блок ({new_block['index']}) с данными успешно добавлен в блокчейн '{blockchain_name}'.[/green]")
    console.print(f"[blue]Время добавления:[/blue] {readable_time}")
    console.print(f"[blue]Хэш нового блока:[/blue] {new_block['hash']}")
    console.print(f"[blue]Хэш предыдущего блока:[/blue] {new_block['previous_hash']}")
    console.print(f"[blue]Добавлен пользователем:[/blue] {new_block['data'].get('added_by')}")

if __name__ == "__main__":
    # Парсинг аргументов командной строки
    parser = argparse.ArgumentParser(description="Добавить данные в блок блокчейна")
    parser.add_argument("--blockchain-name", required=True, help="Имя блокчейна")
    parser.add_argument("--uid", required=True, help="Идентификатор пользователя для авторизации")
    parser.add_argument("data", help="Данные для добавления в новый блок")

    args = parser.parse_args()

    # Добавляем данные в блокчейн
    push_data_to_block(args.blockchain_name, args.uid, args.data)
