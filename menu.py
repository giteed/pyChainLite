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
    console.print()  # Пустая строка
    # Выводим статус тестов
    console.print(test_result_message)

    # Добавляем пустую строку для разделения между тестами и меню
    console.print()

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

    # Определяем ширину таблицы на основе максимальной длины строк
    table_width = max(len(action) for _, action in [("1", "🧱 Создать новый блокчейн"), ("2", "📂 Загрузить блокчейн"),
                                                    ("3", "📜 Список блокчейнов"), ("4", "📝 Создать новый блок"),
                                                    ("5", "🔍 Просмотреть блоки"), ("6", "🧪 Запустить тесты"),
                                                    ("7", "🔄 Обновить проект"), ("H", "❓  Описание функционала"),
                                                    ("Q", "🚪 Выйти")]) + 10  # Задаем ширину с запасом

    console.print(table)  # Выводим таблицу меню

    # Вывод информации о текущем блокчейне перед выбором действия
    if current_blockchain:
        console.print(f"\n[bold green]Текущий блокчейн: {current_blockchain['blocks'][0]['data']['blockchain_name']}[/bold green]")
    else:
        console.print("\n[bold red]Блокчейн не загружен[/bold red]")

def main():
    global current_blockchain

    while True:
        display_menu()
        choice = input("Выберите действие (1-7, H или Q): ").strip().upper()

        if choice == '1':
            create_blockchain()
        elif choice == '2':
            current_blockchain = load_blockchain()  # Сохраняем загруженный блокчейн
        elif choice == '4':
            if current_blockchain:
                create_new_block(current_blockchain)
            else:
                console.print("[bold red]Сначала загрузите блокчейн.[/bold red]")
        elif choice == '5':
            if current_blockchain:
                view_blocks(current_blockchain)
            else:
                console.print("[bold red]Сначала загрузите блокчейн.[/bold red]")
        elif choice == '3':
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
