# modules/blockchain_creation.py
import hashlib
import json
import os
from datetime import datetime
from rich.console import Console

console = Console()

BLOCKCHAIN_DIR = "blockchains"

def create_blockchain(blockchain_name):
    # Генерация хеш-имени файла для блокчейна
    blockchain_file = f"{hashlib.sha256(blockchain_name.encode()).hexdigest()}.json"
    blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)

    # Проверка: если блокчейн с таким именем уже существует
    if os.path.exists(blockchain_path):
        console.print(f"[red]Блокчейн с именем '{blockchain_name}' уже существует. Операция прервана.[/red]")
        return None  # Прерывание

    console.print(f"[green]Имя блокчейна '{blockchain_name}' свободно![/green]")

    # Запрашиваем имя владельца только если блокчейн не существует
    owner_name = input("Введите имя владельца: ")

    # Данные для создания нового блокчейна
    blockchain_data = {
        "name": blockchain_name,
        "blocks": [{
            "index": 0,
            "timestamp": get_current_time(),
            "data": {
                "blockchain_name": blockchain_name,
                "owner": owner_name
            },
            "previous_hash": "0" * 64,
            "hash": hashlib.sha256("genesis".encode()).hexdigest()
        }]
    }

    # Сохраняем блокчейн в файл
    os.makedirs(BLOCKCHAIN_DIR, exist_ok=True)
    with open(blockchain_path, 'w') as f:
        json.dump(blockchain_data, f, indent=4)

    console.print(f"[green]Блокчейн '{blockchain_name}' успешно создан.[/green]")
    return blockchain_data

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
