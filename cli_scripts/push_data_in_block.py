# cli_scripts/push_data_in_block.py
# Скрипт для добавления данных в блок блокчейна через аргументы командной строки
# Пример использования:
# python3 push_data_in_block.py --blockchain-name alfa --uid edd "cli test add data to block" --verbose

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

def debug_message(message, verbose):
    """Вывод отладочных сообщений, если включен режим verbose"""
    if verbose:
        console.print(f"[blue]Отладка:[/blue] {message}")

def push_data_to_block(blockchain_name, user_id, data, verbose=False):
    """
    Добавляет новый блок с данными в существующий блокчейн.
    """
    debug_message(f"Имя блокчейна: {blockchain_name}", verbose)
    debug_message(f"Идентификатор пользователя: {user_id}", verbose)
    debug_message(f"Данные: {data}", verbose)

    if not data.strip():
        console.print("[red]Ошибка: Нельзя добавить блок с пустыми данными![/red]")
        return

    # Получаем хеш имени блокчейна на основе его имени
    blockchain_hash = hashlib.sha256(blockchain_name.encode()).hexdigest()
    debug_message(f"Хэш блокчейна: {blockchain_hash}", verbose)

    blockchain_file = f"{blockchain_hash}.json"
    blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)
    debug_message(f"Абсолютный путь к файлу блокчейна: {blockchain_path}", verbose)

    # Проверяем, существует ли блокчейн
    if not os.path.exists(blockchain_path):
        console.print(f"[red]Ошибка: Блокчейн '{blockchain_name}' не найден по пути: {blockchain_path}[/red]")
        return

    # Загружаем блокчейн
    debug_message("Загружаем блокчейн...", verbose)
    blockchain_data = load_blockchain(blockchain_name)

    if blockchain_data is None:
        console.print(f"[red]Ошибка: Не удалось загрузить данные блокчейна '{blockchain_name}'.[/red]")
        return

    debug_message(f"Данные блокчейна успешно загружены: {blockchain_data}", verbose)

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
    parser.add_argument("--verbose", action="store_true", help="Выводить отладочные сообщения")

    args = parser.parse_args()

    # Добавляем данные в блокчейн
    push_data_to_block(args.blockchain_name, args.uid, args.data, args.verbose)
