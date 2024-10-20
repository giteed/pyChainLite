# menu.py
# Меню pyChainLite

import os
import subprocess
import threading
from rich.console import Console
from rich.table import Table
from modules.blockchain_loading import load_blockchain
from modules.blockchain_listing import list_blockchains
from modules.blockchain_creation import create_blockchain
from modules.block_creation import create_new_block, view_blocks
from modules.update_project import update_project
from modules.run_tests import run_tests
import time

console = Console()
current_blockchain = None  # Переменная для отслеживания текущего блокчейна
test_result_message = "🧪 Запуск тестов..."  # Переменная для хранения результата тестов

# Фоновое выполнение тестов
def background_test_runner():
    global test_result_message
    try:
        # Запускаем тесты, подавляя их вывод
        result = subprocess.run(['pytest'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        if result.returncode == 0:
            # Если тесты прошли успешно
            test_result_message = "🧪 Запуск тестов... [green]OK 👍[/green]"
        else:
            # Если есть ошибки, выводим их перед меню
            test_result_message = "🧪 Запуск тестов... [bold red]Ошибка ❌[/bold red]"
            console.print(f"[bold red]Обнаружены ошибки при тестировании:[/bold red]\n{result.stdout}")
            console.print("Нажмите Enter для продолжения...")
            input()
    except Exception as e:
        # Если произошла ошибка в процессе тестирования
        console.print(f"[bold red]Ошибка при запуске тестов: {e}[/bold red]")

def display_menu():
    menu_width = 50  # Ширина меню для центрирования

    # Основное меню
    table = Table(title="Меню pyChainLite", show_header=True, header_style="bold cyan")
    table.add_column("##", style="dim")
    table.add_column("🚀 Действие", style="bold")

    table.add_row("1", "🧱 Создать новый блокчейн")
    table.add_row("2", "📂 Загрузить блокчейн")
    table.add_row("5", "📜 Список блокчейнов")
    table.add_row("", "")  # Пустая строка для разделения секций
    table.add_row("3", "📝 Создать новый блок")
    table.add_row("4", "🔍 Просмотреть блоки")
    table.add_row("", "")  # Пустая строка для разделения секций
    table.add_row("6", "🧪 Запустить тесты")
    table.add_row("", "")  # Пустая строка для разделения секций
    table.add_row("7", "🔄 Обновить проект")
    table.add_row("H", "❓  Описание функционала")
    table.add_row("Q", "🚪 Выйти")

    # Центрирование информации о блокчейне после меню
    console.print(table)

    # Центрирование информации о статусе тестов
    test_status = test_result_message.center(menu_width)
    console.print(test_status)

    # Центрирование информации о блокчейне
    if current_blockchain:
        blockchain_info = f"Текущий блокчейн: {current_blockchain['blocks'][0]['data']['blockchain_name']}"
    else:
        blockchain_info = "Блокчейн не загружен"

    blockchain_status = blockchain_info.center(menu_width)
    console.print(blockchain_status)


def main():
    global current_blockchain

    # Запускаем тесты в фоне
    test_thread = threading.Thread(target=background_test_runner)
    test_thread.start()

    # Ожидаем завершения тестов перед тем, как показать меню
    test_thread.join()

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
