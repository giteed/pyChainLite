# menu.py
# Главное меню для взаимодействия с pyChainLite

import os
from rich.console import Console
from modules.blockchain_creation import create_blockchain
from modules.blockchain_loading import load_blockchain
from modules.blockchain_listing import list_blockchains
from modules.block_creation import create_new_block
from modules.block_viewer import view_blocks
from modules.run_tests import run_tests
from modules.update_project import update_project
from modules.menu_help import display_help_menu  # Исправлен импорт

console = Console()

def main():
    current_blockchain = None

    while True:
        console.print(f"\n[bold]Текущий блокчейн:[/bold] [cyan]{current_blockchain['name'] if current_blockchain else 'Блокчейн не загружен'}[/cyan]")
        console.print()
        
        # Основное меню
        console.print("         Меню pyChainLite         ")
        console.print("┏━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        console.print("┃ ## ┃ 🚀 Выберите действие      ┃")
        console.print("┡━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━┩")
        console.print("│ 1  │ 🧱 Создать новый блокчейн │")
        console.print("│ 2  │ 📂 Загрузить блокчейн     │")
        console.print("│ 3  │ 📜 Список блокчейнов      │")
        console.print("│    │                           │")
        console.print("│ 4  │ 📝 Создать новый блок     │")
        console.print("│ 5  │ 🔍 Просмотреть блоки      │")
        console.print("│    │                           │")
        console.print("│ 6  │ 🧪 Запустить тесты        │")
        console.print("│    │                           │")
        console.print("│ 7  │ 🔄 Обновить проект        │")
        console.print("│ H  │ ❓ Описание функционала   │")
        console.print("│    │                           │")
        console.print("│ Q  │ 🚪 Выйти                  │")
        console.print("└────┴───────────────────────────┘")

        choice = input("\nВведите ваш выбор: ").strip().lower()

        if choice == '1':
            blockchain_name = input("Введите имя нового блокчейна: ")
            owner_name = input("Введите имя владельца: ")
            current_blockchain = create_blockchain(blockchain_name, owner_name)
            console.print(f"Блокчейн '{blockchain_name}' успешно создан.")
        
        elif choice == '2':
            blockchain_name = input("Введите имя блокчейна для загрузки: ")
            current_blockchain = load_blockchain(blockchain_name)
            if current_blockchain:
                console.print(f"Блокчейн '{blockchain_name}' успешно загружен.")
            else:
                console.print(f"[red]Ошибка загрузки блокчейна '{blockchain_name}'.[/red]")
        
        elif choice == '3':
            list_blockchains()
        
        elif choice == '4':
            if current_blockchain:
                block_data = input("Введите данные для нового блока: ")
                create_new_block(current_blockchain, block_data)  # Передаем блокчейн и данные блока
                console.print(f"Новый блок успешно добавлен в блокчейн '{current_blockchain['name']}'.")
            else:
                console.print("[red]Блокчейн не загружен. Сначала загрузите блокчейн.[/red]")
        
        elif choice == '5':
            if current_blockchain:
                view_blocks(current_blockchain)
            else:
                console.print("[red]Блокчейн не загружен. Сначала загрузите блокчейн.[/red]")

        elif choice == '6':
            run_tests()
        
        elif choice == '7':
            update_project()

        elif choice == 'h':
            display_help_menu()  # Вызов функции для отображения помощи

        elif choice == 'q':
            console.print("Выход...")
            break

        else:
            console.print("[red]Неверный выбор. Попробуйте снова.[/red]")

if __name__ == "__main__":
    main()
