# modules/blockchain_loading.py
# Модуль для загрузки блокчейна
import os
import json
import hashlib
from rich.console import Console

console = Console()
BLOCKCHAIN_DIR = "blockchains"

def load_blockchain():
    blockchain_name = input("Введите имя блокчейна для загрузки: ").strip()
    if not blockchain_name:
        console.print("[red]Имя блокчейна не может быть пустым.[/red]")
        return None

    blockchain_hash = hashlib.sha256(blockchain_name.encode()).hexdigest()
    blockchain_file = f"{blockchain_hash}.json"
    blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)

    if not os.path.exists(blockchain_path):
        console.print(f"[red]Блокчейн с именем '{blockchain_name}' не найден.[/red]")
        return None

    with open(blockchain_path, 'r') as f:
        blockchain_data = json.load(f)

    console.print(f"\nБлокчейн '{blockchain_name}' загружен.")
    console.print(json.dumps(blockchain_data, indent=4))

    blockchain_data["file"] = blockchain_file  # Добавляем путь к файлу в загруженные данные
    return blockchain_data
