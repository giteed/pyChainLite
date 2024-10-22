# modules/block_creation.py
# Модуль для создания нового блокчейна и добавления нового блока в существующий блокчейн
# Этот модуль содержит функции для создания нового блокчейна и добавления блоков в существующую цепочку.
# Пример использования:
# create_blockchain("my_chain", "owner_name") - создаст новый блокчейн.
# create_new_block(blockchain_data, data, user_id="user_id") - добавит новый блок в цепочку.

import hashlib
import json
import os
from datetime import datetime
from rich.console import Console
from modules.debug import debug  # Импортируем функцию для управления отладкой

console = Console()

# Путь к папке с блокчейнами
BLOCKCHAIN_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "blockchains")

def create_blockchain(blockchain_name, owner_name):
    """
    Создает новый блокчей с указанным именем и владельцем.
    """
    # Проверяем наличие директории для хранения блокчейнов
    if not os.path.exists(BLOCKCHAIN_DIR):
        os.makedirs(BLOCKCHAIN_DIR)
        debug_message(f"Папка для блокчейнов создана: {BLOCKCHAIN_DIR}", verbose=True)  # Управляем отладочным сообщением

    # Генерируем хеш для имени блокчейна
    blockchain_hash = hashlib.sha256(blockchain_name.encode()).hexdigest()
    blockchain_file = f"{blockchain_hash}.json"
    blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)

    # Проверяем, существует ли уже блокчейн с таким именем
    if os.path.exists(blockchain_path):
        console.print(f"[red]Ошибка: Блокчейн с именем '{blockchain_name}' уже существует.[/red]")
        return None

    # Генезис блок (первый блок)
    genesis_block = {
        "index": 0,
        "timestamp": datetime.now().isoformat(),
        "data": {
            "blockchain_name": blockchain_name,
            "owner": owner_name
        },
        "previous_hash": "0" * 64,
        "hash": ""
    }

    # Вычисляем хеш генезис-блока
    genesis_block_content = json.dumps(genesis_block, sort_keys=True).encode()
    genesis_block["hash"] = hashlib.sha256(genesis_block_content).hexdigest()

    # Создаем структуру блокчейна
    blockchain_data = {
        "name": blockchain_name,
        "blocks": [genesis_block]
    }

    # Сохраняем блокчейн в файл
    with open(blockchain_path, 'w') as f:
        json.dump(blockchain_data, f, indent=4)

    console.print(f"[green]Блокчейн '{blockchain_name}' успешно создан.[/green]")
    return blockchain_data


def create_new_block(blockchain_data, data, user_id):
    """
    Создает новый блок и добавляет его в цепочку.
    """
    # Отладка: получение последнего блока
    last_block = blockchain_data["blocks"][-1]
    debug_message(f"Последний блок в цепочке: {last_block}", verbose=True)  # Управляем отладочным сообщением

    # Новый блок
    new_block = {
        "index": last_block["index"] + 1,
        "timestamp": datetime.now().timestamp(),
        "data": {
            "data": data,
            "added_by": user_id,
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        },
        "previous_hash": last_block["hash"]
    }

    # Вычисляем хеш нового блока
    block_content = json.dumps(new_block, sort_keys=True).encode()
    new_block["hash"] = hashlib.sha256(block_content).hexdigest()

    # Добавляем новый блок в блокчейн
    blockchain_data["blocks"].append(new_block)

    # Определяем путь к файлу блокчейна (абсолютный путь)
    blockchain_hash = hashlib.sha256(blockchain_data["name"].encode()).hexdigest()
    blockchain_file = f"{blockchain_hash}.json"
    blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)

    # Проверяем, существует ли директория для блокчейнов
    if not os.path.exists(BLOCKCHAIN_DIR):
        os.makedirs(BLOCKCHAIN_DIR)

    # Отладка: путь к файлу блокчейна
    debug_message(f"Путь к файлу блокчейна для записи: {blockchain_path}", verbose=True)  # Управляем отладочным сообщением

    # Сохраняем блокчейн в файл
    try:
        with open(blockchain_path, 'w') as f:
            json.dump(blockchain_data, f, indent=4)
        console.print(f"[green]Новый блок успешно добавлен в блокчейн '{blockchain_data['name']}'[/green]")
    except Exception as e:
        console.print(f"[red]Ошибка при сохранении блока: {e}[/red]")

    return new_block
