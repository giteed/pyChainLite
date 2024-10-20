# menu.py
# Меню pyChainLite
# Назначение: Управление блокчейнами и блоками, запуск тестов, обновление проекта

import os
import subprocess
import shutil
import json
import hashlib
from rich.console import Console
from rich.table import Table
from modules.blockchain_creation import create_blockchain
from modules.blockchain_loading import load_blockchain
from modules.block_creation import create_new_block
from modules.block_viewer import view_blocks
from modules.blockchain_listing import list_blockchains
from modules.run_tests import run_tests
from modules.update_project import update_project

console = Console()

current_blockchain = None  # Переменная для хранения текущего блокчейна

# Основное меню
def display_menu():
    table = Table(title="Меню pyChainLite", show_header=True, header_style="bold cyan")
    table.add_column("##", style="dim")
    table.add_column("Действие", style="bold")

    # Работа с блокчейнами
    table.add_row("1", "🧱 Создать новый блокчейн")
    table.add_row("2", "📂 Загрузить блокчейн")
    table.add_row("3", "📜 Список блокчейнов")

    # Разделительная линия
    table.add_row("", "")

    # Работа с блоками
    table.add_row("4", "📝 Создать новый блок")
    table.add_row("5", "🔍 Просмотреть блоки")

    # Разделительная линия
    table.add_row("", "")

    # Тестирование
    table.add_row("6", "🧪 Запустить тесты")

    # Разделительная линия
    table.add_row("", "")

    # Обновление
    table.add_row("7", "🔄 Обновить проект")

    # Выход
    table.add_row("Q", "🚪 Выйти")

    console.print(table)

# Основной цикл программы
def main():
    global current_blockchain
    while True:
        display_menu()
        choice = input("Выберите действие (1-7 или Q): ").strip().upper()
        
        if choice == '1':
            create_blockchain()
        elif choice == '2':
            current_blockchain = load_blockchain()
        elif choice == '3':
            list_blockchains()
        elif choice == '4':
            if current_blockchain:
                create_new_block(current_blockchain)
            else:
                console.print("[red]Сначала загрузите блокчейн.[/red]")
        elif choice == '5':
            if current_blockchain:
                view_blocks(current_blockchain)
            else:
                console.print("[red]Сначала загрузите блокчейн.[/red]")
        elif choice == '6':
            run_tests()
        elif choice == '7':
            update_project()
        elif choice == 'Q':
            console.print("[bold green]Выход...[/bold green]")
            break
        else:
            console.print("[bold red]Неверный выбор. Пожалуйста, выберите действие от 1 до 7 или Q.[/bold red]")

if __name__ == "__main__":
    main()
