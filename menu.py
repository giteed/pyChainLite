# menu.py
# Основное меню для управления блокчейном pyChainLite

import os
import json
import hashlib
from rich.console import Console
from modules.blockchain_loading import load_blockchain
from modules.block_creation import create_new_block
from modules.blockchain_listing import list_blockchains
from modules.blockchain_creation import create_blockchain

console = Console()

BLOCKCHAIN_DIR = "blockchains"
current_blockchain = None


def main():
    global current_blockchain

    while True:
        console.print(f"\n[bold]Текущий блокчейн:[/bold] [cyan]{current_blockchain['name'] if current_blockchain else 'Блокчейн не загружен'}[/cyan]")
        
        console.print(
            "\n         [bold]Меню pyChainLite[/bold]         \n"
            "┏━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n"
            "┃ ## ┃ 🚀 Выберите действие      ┃\n"
            "┡━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━┩\n"
            "│ 1  │ 🧱 Создать новый блокчейн │\n"
            "│ 2  │ 📂 Загрузить блокчейн     │\n"
            "│ 3  │ 📜 Список блокчейнов      │\n"
            "│    │                           │\n"
            "│ 4  │ 📝 Создать новый блок     │\n"
            "│ 5  │ 🔍 Просмотреть блоки      │\n"
            "│    │                           │\n"
            "│ 6  │ 🧪 Запустить тесты        │\n"
            "│    │                           │\n"
            "│ 7  │ 🔄 Обновить проект        │\n"
            "│ H  │ ❓ Описание функционала   │\n"
            "│    │                           │\n"
            "│ Q  │ 🚪 Выйти                  │\n"
            "└────┴───────────────────────────┘"
        )

        choice = input("\nВведите ваш выбор: ").lower()

        if choice == "1":
            blockchain_name = input("Введите имя нового блокчейна: ")
            owner_name = input("Введите имя владельца: ")
            current_blockchain = create_blockchain(blockchain_name, owner_name)
        elif choice == "2":
            blockchain_name = input("Введите имя блокчейна для загрузки: ")
            current_blockchain = load_blockchain(blockchain_name)
        elif choice == "3":
            list_blockchains()
        elif choice == "4":
            if current_blockchain:
                data = input("Введите данные для нового блока: ")
                create_new_block(current_blockchain, data)
            else:
                console.print("[bold red]Ошибка:[/bold red] Блокчейн не загружен. Пожалуйста, загрузите блокчейн.")
        elif choice == "5":
            if current_blockchain:
                for block in current_blockchain["blocks"]:
                    console.print(f"Блок {block['index']}: {block}")
            else:
                console.print("[bold red]Ошибка:[/bold red] Блокчейн не загружен.")
        elif choice == "6":
            run_tests()
        elif choice == "7":
            update_project()
        elif choice == "h":
            show_help()
        elif choice == "q":
            console.print("Выход...")
            break
        else:
            console.print("[bold red]Ошибка:[/bold red] Неверный выбор. Пожалуйста, выберите действие из списка.")


def run_tests():
    import subprocess
    try:
        console.print("🧪 Запуск тестов...")
        subprocess.run(["pytest"], check=True)
        console.print("🧪 Тесты завершены успешно! OK 👍")
    except subprocess.CalledProcessError:
        console.print("[bold red]Ошибка при запуске тестов.[/bold red]")


def update_project():
    import subprocess
    try:
        console.print("🔄 [bold cyan]Запуск обновления проекта...[/bold cyan]")
        subprocess.run(["git", "pull"], check=True)
        console.print("Проект успешно обновлен.")
    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]Ошибка при обновлении проекта: {e}[/bold red]")


def show_help():
    console.print("Описание функционала программы:")
    console.print("1. Создание нового блокчейна")
    console.print("2. Загрузка существующего блокчейна")
    console.print("3. Просмотр списка блокчейнов")
    console.print("4. Добавление нового блока в блокчейн")
    console.print("5. Просмотр блоков в загруженном блокчейне")
    console.print("6. Запуск тестов для проверки функциональности")
    console.print("7. Обновление проекта с GitHub")


if __name__ == "__main__":
    main()
