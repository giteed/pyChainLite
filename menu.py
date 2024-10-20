# menu.py
# Меню pyChainLite

import os
from rich.console import Console
from rich.table import Table
from modules.blockchain_loading import load_blockchain
from modules.blockchain_listing import list_blockchains
from modules.blockchain_creation import create_blockchain
from modules.block_creation import create_new_block, view_blocks
from modules.update_project import update_project
from modules.run_tests import run_tests
from modules.help_menu import display_help_menu

console = Console()
current_blockchain = None  # Переменная для отслеживания текущего блокчейна
test_result_message = "🧪 Запуск тестов... [green]OK 👍[/green]"

def display_menu():
    # Основное меню
    table = Table(title="Меню pyChainLite", show_header=True, header_style="bold cyan")
    table.add_column("##", style="dim")
    table.add_column("🚀 Действие", style="bold")
    
    table.add_row("1", "🧱 Создать новый блокчейн")
    table.add_row("2", "📂 Загрузить блокчейн")
    table.add_row("3", "📜 Список блокчейнов")
    table.add_row("", "")  # Пустая строка для разделения секций
    table.add_row("4", "📝 Создать новый блок")
    table.add_row("5", "🔍 Просмотреть блоки")
    table.add_row("", "")  # Пустая строка для разделения секций
    table.add_row("6", "🧪 Запустить тесты")
    table.add_row("", "")  # Пустая строка для разделения секций
    table.add_row("7", "🔄 Обновить проект")
    table.add_row("H", "❓  Описание функционала")
    table.add_row("Q", "🚪 Выйти")
    
    console.print(table)

def main():
    global current_blockchain

    while True:
        console.print("")  # Добавим пустую строку для разделения тестов
        if current_blockchain:
            console.print(f"Текущий блокчейн: [bold green]{current_blockchain['blocks'][0]['data']['blockchain_name']}[/bold green]")
        else:
            console.print("[bold red]Блокчейн не загружен[/bold red]")

        display_menu()
        
        choice = input("Выберите действие (1-7, H или Q): ").strip().upper()
        
        # Обрабатываем выбор пользователя...

def main():
    global current_blockchain

    while True:
        display_menu()
        choice = input("Выберите действие (1-7, H или Q): ").strip().upper()

        if choice == '1':
            create_blockchain()
        elif choice == '2':
            current_blockchain = load_blockchain()  # Сохраняем загруженный блокчейн
        elif choice == '3':
            if current_blockchain:
                create_new_block(current_blockchain)
            else:
                console.print("[bold red]Сначала загрузите блокчейн.[/bold red]")
        elif choice == '4':
            if current_blockchain:
                view_blocks(current_blockchain)
            else:
                console.print("[bold red]Сначала загрузите блокчейн.[/bold red]")
        elif choice == '5':
            list_blockchains()
        elif choice == '6':
            run_tests()
        elif choice == '7':
            update_project()
        elif choice == 'H':
            display_help_menu()  # Вызов меню помощи
        elif choice == 'Q':
            console.print("[bold green]Выход...[/bold green]")
            break
        else:
            console.print("[bold red]Неверный выбор. Пожалуйста, выберите действие от 1 до 7, H или Q.[/bold red]")

if __name__ == "__main__":
    main()
