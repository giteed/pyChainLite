# menu.py
# Меню pyChainLite
import os
import subprocess
import json
from rich.console import Console
from rich.table import Table

from modules.blockchain_creation import create_blockchain
from modules.blockchain_loading import load_blockchain
from modules.block_creation import create_new_block
from modules.blockchain_listing import list_blockchains
from modules.block_viewer import view_blocks
from modules.update_project import update_project
from modules.run_tests import run_tests

console = Console()

# Основное меню
def display_menu():
    table = Table(title="Меню pyChainLite", show_header=True, header_style="bold cyan")
    table.add_column("Номер", style="dim")
    table.add_column("Действие", style="bold")
    
    # Блок 1: Блокчейны
    table.add_row("1", "🧱 Создать новый блокчейн")
    table.add_row("2", "📂 Загрузить блокчейны")
    
    # Блок 2: Блоки
    table.add_row("3", "📝 Создать новый блок")
    table.add_row("4", "🔍 Просмотреть блоки")

    # Блок 3: Тесты
    table.add_row("5", "🧪 Запустить тесты")

    # Блок 4: Обновление
    table.add_row("6", "🔄 Обновить проект")

    # Выход
    table.add_row("Q", "🚪 Выйти")

    console.print(table)

# Основной цикл программы
def main():
    while True:
        display_menu()
        choice = input("Выберите действие (1-6 или Q): ").strip().lower()
        
        if choice == '1':
            create_blockchain()
        elif choice == '2':
            load_blockchain()
        elif choice == '3':
            create_new_block()
        elif choice == '4':
            view_blocks()
        elif choice == '5':
            run_tests()
        elif choice == '6':
            update_project()
        elif choice == 'q':
            console.print("[bold green]Выход...[/bold green]")
            break
        else:
            console.print("[bold red]Неверный выбор. Пожалуйста, выберите действие от 1 до 6 или Q для выхода.[/bold red]")

if __name__ == "__main__":
    main()
