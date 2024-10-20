# menu.py
# Меню pyChainLite
from rich.console import Console
from rich.table import Table
import os
import subprocess
import shutil

console = Console()

# Функция для создания и отображения меню
def display_menu():
    table = Table(title="Меню pyChainLite", show_header=False, header_style="bold cyan")
    
    # Блок 1 - Блокчейны
    table.add_row("[bold]Блокчейны:[/bold]")
    table.add_row("1", "🧱 Создать новый блокчейн")
    table.add_row("2", "📂 Загрузить блокчейн")

    # Блок 2 - Блоки
    table.add_row("")
    table.add_row("[bold]Блоки:[/bold]")
    table.add_row("3", "📝 Создать новый блок")
    table.add_row("4", "🔍 Просмотреть блоки")

    # Блок 3 - Тестирование
    table.add_row("")
    table.add_row("[bold]Тестирование:[/bold]")
    table.add_row("5", "🧪 Запустить тесты")

    # Блок 4 - Обновление проекта
    table.add_row("")
    table.add_row("[bold]Обновление:[/bold]")
    table.add_row("6", "🔄 Обновить проект")

    # Блок 5 - Выход
    table.add_row("")
    table.add_row("q", "🚪 Выйти")

    console.print(table)

# Функция для создания нового блокчейна (пока только заглушка)
def create_blockchain():
    console.print("🧱 [bold green]Создание нового блокчейна...[/bold green]")
    # Логика создания блокчейна здесь

# Функция для загрузки существующего блокчейна (пока только заглушка)
def load_blockchain():
    console.print("📂 [bold green]Загрузка блокчейна...[/bold green]")
    # Логика загрузки блокчейна здесь

# Функция для создания нового блока (пока только заглушка)
def create_new_block():
    console.print("📝 [bold green]Создание нового блока...[/bold green]")
    # Логика создания нового блока здесь

# Функция для просмотра блоков (пока только заглушка)
def view_blocks():
    console.print("🔍 [bold green]Просмотр блоков...[/bold green]")
    # Логика просмотра блоков здесь

# Функция для запуска тестов (пока только заглушка)
def run_tests():
    console.print("🧪 [bold green]Запуск тестов...[/bold green]")
    # Логика запуска тестов здесь

# Функция для обновления проекта (пока только заглушка)
def update_project():
    console.print("🔄 [bold cyan]Запуск обновления проекта...[/bold cyan]")
    # Логика обновления проекта здесь

# Основной цикл программы
def main():
    while True:
        display_menu()
        choice = input("Выберите действие (1-6 или q для выхода): ").strip().lower()
        
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
            console.print("[bold red]Неверный выбор. Пожалуйста, выберите действие от 1 до 6 или q для выхода.[/bold red]")

if __name__ == "__main__":
    main()
