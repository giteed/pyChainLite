# menu.py
import os
import subprocess
from rich.console import Console
from rich.table import Table
from modules.blockchain_creation import create_blockchain
from modules.blockchain_loading import load_blockchain
from modules.block_creation import create_new_block
from modules.blockchain_listing import list_blockchains
from modules.block_viewer import view_blocks
from modules.update_project import update_project

console = Console()

# Основное меню
def display_menu():
    table = Table(title="Меню pyChainLite", show_header=True, header_style="bold cyan")
    table.add_column("Номер", style="dim")
    table.add_column("Действие", style="bold")

    table.add_row("1", "Создать новый блокчейн")
    table.add_row("2", "Загрузить блокчейн")
    table.add_row("3", "Создать новый блок")
    table.add_row("4", "Просмотреть блоки")
    table.add_row("5", "Список блокчейнов")
    table.add_row("6", "Запустить тесты")  # Пункт для тестов возвращен
    table.add_row("7", "Обновить проект")
    table.add_row("8", "Выйти")

    console.print(table)

# Функция для запуска тестов
def run_tests():
    console.print("🧪 [bold magenta]Запуск тестов...[/bold magenta]")
    try:
        subprocess.run(['pytest'], check=True)
    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]Ошибка при запуске тестов: {e}[/bold red]")

# Основной цикл программы
def main():
    while True:
        display_menu()
        choice = input("Выберите действие (1-8): ").strip()

        if choice == '1':
            create_blockchain()
        elif choice == '2':
            load_blockchain()
        elif choice == '3':
            create_new_block()
        elif choice == '4':
            view_blocks()
        elif choice == '5':
            list_blockchains()
        elif choice == '6':
            run_tests()  # Пункт для запуска тестов
        elif choice == '7':
            update_project()
        elif choice == '8':
            console.print("[bold green]Выход...[/bold green]")
            break
        else:
            console.print("[bold red]Неверный выбор. Пожалуйста, выберите действие от 1 до 8.[/bold red]")

if __name__ == "__main__":
    main()
