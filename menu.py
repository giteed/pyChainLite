# menu.py
# Меню pyChainLite
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
    table.add_column("Номер", style="dim")
    table.add_column("Действие", style="bold")
    
    # Блоки меню
    table.add_row("1", "🧱 Создать новый блокчейн")
    table.add_row("2", "📂 Загрузить блокчейны")
    table.add_row("3", "📝 Создать новый блок")
    table.add_row("4", "🔍 Просмотреть блоки")
    table.add_row("5", "📜 Список блокчейнов")
    table.add_row("6", "🧪 Запустить тесты")
    table.add_row("7", "🔄 Обновить проект")
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
            if current_blockchain:
                create_new_block(current_blockchain)
            else:
                console.print("[red]Сначала загрузите блокчейн.[/red]")
        elif choice == '4':
            if current_blockchain:
                view_blocks(current_blockchain)
            else:
                console.print("[red]Сначала загрузите блокчейн.[/red]")
        elif choice == '5':
            list_blockchains()
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
