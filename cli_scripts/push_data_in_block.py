# cli_scripts/push_data_in_block.py
# Скрипт для добавления данных в блок блокчейна через аргументы командной строки с улучшенной справкой

import argparse
import os
import json
import sys
import hashlib
from datetime import datetime
from rich.console import Console
from rich.text import Text

console = Console()

# Добавляем путь к модулям в системный путь
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from modules.blockchain_loading import load_blockchain
from modules.block_creation import create_new_block

BLOCKCHAIN_DIR = "blockchains"  # Путь к папке с блокчейнами

def push_data_to_block(blockchain_name, user_id, data):
    """
    Функция для добавления данных в блокчейн.
    
    :param blockchain_name: Имя блокчейна
    :param user_id: Идентификатор пользователя (владелец блокчейна)
    :param data: Данные для добавления в новый блок
    """
    
    # Проверяем, введены ли данные
    if not data.strip():
        console.print("[red]Ошибка: данные для добавления не могут быть пустыми.[/red]")
        return

    # Получаем хеш имени блокчейна на основе его имени
    blockchain_hash = hashlib.sha256(blockchain_name.encode()).hexdigest()
    blockchain_file = f"{blockchain_hash}.json"
    blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)

    # Проверяем, существует ли блокчейн
    if not os.path.exists(blockchain_path):
        console.print(f"[red]Ошибка: Блокчейн '{blockchain_name}' не найден.[/red]")
        return

    # Загружаем блокчейн
    with open(blockchain_path, 'r') as f:
        blockchain_data = json.load(f)

    # Проверяем, есть ли у пользователя права на запись в блокчейн
    if user_id != blockchain_data["blocks"][0]["data"]["owner"]:
        console.print(f"[red]Ошибка: Пользователь '{user_id}' не имеет прав на запись в этот блокчейн.[/red]")
        return

    # Добавляем новый блок с переданными данными и идентификатором пользователя
    new_block = create_new_block(blockchain_data, data, user_id=user_id)

    # Преобразуем timestamp в читаемый формат
    readable_time = datetime.fromtimestamp(float(new_block["timestamp"])).strftime('%Y-%m-%d %H:%M:%S')

    # Сохраняем обновленный блокчейн
    with open(blockchain_path, 'w') as f:
        json.dump(blockchain_data, f, indent=4)

    # Выводим информацию о новом блоке
    console.print(f"[green]Новый блок ({new_block['index']}) с данными успешно добавлен в блокчейн '{blockchain_name}'.[/green]")
    console.print(f"Время добавления: [cyan]{readable_time}[/cyan]")
    console.print(f"Хэш нового блока: [yellow]{new_block['hash']}[/yellow]")
    console.print(f"Хэш предыдущего блока: [yellow]{new_block['previous_hash']}[/yellow]")
    console.print(f"Добавлен пользователем: [bold]{new_block['data']['added_by']}[/bold]")

def display_help():
    """
    Расширенная справка по работе с командной строкой для добавления данных в блокчейн.
    """
    console.print("\n[bold]Помощь по использованию скрипта push_data_in_block.py[/bold]", style="bold underline")
    
    console.print("\n[cyan]Описание:[/cyan]")
    console.print("Этот скрипт позволяет добавлять данные в блокчейн, используя командную строку.")
    
    console.print("\n[cyan]Как использовать:[/cyan]")
    console.print("Для запуска скрипта используйте следующую команду:")
    console.print("[bold yellow]python3 push_data_in_block.py --blockchain-name <имя_блокчейна> --uid <имя_пользователя> <данные>[/bold yellow]\n")
    
    console.print("[cyan]Аргументы командной строки:[/cyan]")
    table = Text()
    table.append("[bold]--blockchain-name[/bold]:   ", style="bold yellow")
    table.append("Имя существующего блокчейна, куда нужно добавить новый блок.\n")
    table.append("[bold]--uid[/bold]:              ", style="bold yellow")
    table.append("Имя пользователя (владельца блокчейна), который добавляет данные.\n")
    table.append("[bold]<данные>[/bold]:           ", style="bold yellow")
    table.append("Данные, которые нужно добавить в новый блок.\n")
    console.print(table)
    
    console.print("\n[cyan]Пример использования:[/cyan]")
    console.print("1. Добавление данных в блокчейн с именем 'myblockchain' от пользователя 'edd':\n")
    console.print("[bold yellow]python3 push_data_in_block.py --blockchain-name myblockchain --uid edd 'Это данные для нового блока'[/bold yellow]\n")
    
    console.print("2. Если вы не хотите добавлять пустые данные, система сообщит об ошибке:")
    console.print("[bold red]Ошибка: данные для добавления не могут быть пустыми.[/bold red]\n")

    console.print("\n[bold]Примечание:[/bold] Все данные должны быть корректными и права пользователя должны быть проверены.\n")
    
    console.print("[cyan]Дополнительная информация:[/cyan]")
    console.print("Перед добавлением убедитесь, что блокчейн уже существует и вы являетесь его владельцем.")

if __name__ == "__main__":
    # Парсинг аргументов командной строки
    parser = argparse.ArgumentParser(description="Добавить данные в блок блокчейна")
    parser.add_argument("--blockchain-name", required=True, help="Имя блокчейна")
    parser.add_argument("--uid", required=True, help="Идентификатор пользователя для авторизации")
    parser.add_argument("data", help="Данные для добавления в новый блок")
    parser.add_argument("--help-cli", action="store_true", help="Показать помощь по работе с командной строкой")

    args = parser.parse_args()

    # Проверка на вывод справки по CLI
    if args.help_cli:
        display_help()
    else:
        # Добавляем данные в блокчейн
        push_data_to_block(args.blockchain_name, args.uid, args.data)
