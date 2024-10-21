# modules/blockchain_loading.py
# Модуль для загрузки блокчейна

import os
import json
import hashlib
from rich.console import Console

console = Console()

# Путь к папке с блокчейнами
BLOCKCHAIN_DIR = "blockchains"

def load_blockchain(blockchain_name):
    """
    Загружает блокчейн из файла.
    Возвращает данные блокчейна или None, если файл не найден.
    """
    # Формируем имя файла на основе хеша блокчейна
    blockchain_hash = hashlib.sha256(blockchain_name.encode()).hexdigest()
    blockchain_file = f"{blockchain_hash}.json"
    blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)

    # Отладочная информация
    console.print(f"[blue]Отладка:[/blue] Пытаемся загрузить блокчейн из файла: {blockchain_path}")

    # Проверяем, существует ли файл
    if not os.path.exists(blockchain_path):
        console.print(f"[red]Ошибка: Файл блокчейна не найден: {blockchain_path}[/red]")
        return None

    # Пытаемся загрузить файл блокчейна
    try:
        with open(blockchain_path, 'r') as f:
            blockchain_data = json.load(f)
            # Отладочная информация
            console.print(f"[blue]Отладка:[/blue] Данные блокчейна успешно загружены: {blockchain_data}")
            return blockchain_data
    except json.JSONDecodeError as e:
        console.print(f"[red]Ошибка: Не удалось декодировать JSON из файла блокчейна: {e}[/red]")
        return None
    except Exception as e:
        console.print(f"[red]Ошибка: Не удалось загрузить блокчейн: {e}[/red]")
        return None
