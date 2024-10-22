# modules/blockchain_loading.py
# Модуль для загрузки блокчейна

import os
import json
import hashlib
from rich.console import Console
from modules.debug import debug  # Импортируем функцию для отладочных сообщений

console = Console()

# Определяем путь к корневой директории
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOCKCHAIN_DIR = os.path.join(ROOT_DIR, "blockchains")

def load_blockchain(blockchain_name):
    """
    Загружает блокчейн из файла.
    Возвращает данные блокчейна или None, если файл не найден.
    """
    # Формируем имя файла на основе хеша блокчейна
    blockchain_hash = hashlib.sha256(blockchain_name.encode()).hexdigest()
    blockchain_file = f"{blockchain_hash}.json"
    blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)

    debug(f"Пытаемся загрузить блокчейн из файла: {blockchain_path}")

    # Проверяем, существует ли файл
    if not os.path.exists(blockchain_path):
        console.print(f"[red]Ошибка: Файл блокчейна не найден: {blockchain_path}[/red]")
        return None

    # Пытаемся загрузить файл блокчейна
    try:
        with open(blockchain_path, 'r') as f:
            blockchain_data = json.load(f)
            debug(f"Данные блокчейна успешно загружены: {blockchain_data}")
            return blockchain_data
    except json.JSONDecodeError as e:
        console.print(f"[red]Ошибка: Не удалось декодировать JSON из файла блокчейна: {e}[/red]")
        return None
    except Exception as e:
        console.print(f"[red]Ошибка: Не удалось загрузить блокчейн: {e}[/red]")
        return None
