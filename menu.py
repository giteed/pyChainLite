# menu.py
# Главное меню для взаимодействия с pyChainLite
# Этот скрипт отвечает за отображение главного меню, управление действиями пользователя и взаимодействие с различными модулями pyChainLite.
# Пользователь может создавать новые блокчейны, загружать существующие, просматривать список блоков, запускать тесты и обновлять проект.

import os
from rich.console import Console
from modules.blockchain_creation import create_blockchain
from modules.blockchain_loading import load_blockchain
from modules.blockchain_listing import list_blockchains
from modules.block_creation import create_new_block
from modules.block_viewer import view_blocks
from modules.run_tests import run_tests
from modules.update_project import update_project
from modules.menu_help import display_help_menu

console = Console()
BLOCKCHAIN_DIR = "blockchains"
current_blockchain = None

def main():
    global current_blockchain

    while True:
        console.print(f"\n[bold]Текущий блокчейн:[/bold] [cyan]{current_blockchain['name'] if current_blockchain else 'Блокчейн не загружен'}[/cyan]")

        # Отображение меню
        console.print("""
         Меню pyChainLite         
┏━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ ## ┃ 🚀 Выберите действие      ┃
┡━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 1  │ 🧱 Создать новый блокчейн │
│ 2  │ 📂 Загрузить блокчейн     │
│ 3  │ 📜 Список блокчейнов      │
│    │                           │
│ 4  │ 📝 Создать новый блок     │
│ 5  │ 🔍 Просмотреть блоки      │
│    │                           │
│ 6  │ 🧪 Запустить тесты        │
│    │                           │
│ 7  │ 🔄 Обновить проект        │
│ H  │ ❓ Описание функционала   │
│    │                           │
│ Q  │ 🚪 Выйти                  │
└────┴───────────────────────────┘
        """)

        # Получение выбора пользователя
        choice = input("Введите ваш выбор: ").strip().upper()

        # Обработка выбора пользователя
        if choice == '1':
            blockchain_name = input("Введите имя нового блокчейна: ").strip()
            
            # Проверка на существование блокчейна
            if blockchain_exists(blockchain_name):
                console.print(f"[red]Блокчейн с именем '{blockchain_name}' уже существует. Операция прервана.[/red]")
                continue
            
            owner_name = input("Введите имя владельца: ").strip()
            current_blockchain = create_blockchain(blockchain_name, owner_name)
            console.print(f"[green]Блокчейн '{blockchain_name}' успешно создан.[/green]")

        elif choice == '2':
            blockchain_name = input("Введите имя блокчейна для загрузки: ").strip()
            current_blockchain = load_blockchain(blockchain_name)
            if current_blockchain:
                console.print(f"[green]Блокчейн '{blockchain_name}' успешно загружен.[/green]")
            else:
                console.print(f"[red]Ошибка: Блокчейн '{blockchain_name}' не найден.[/red]")

        elif choice == '3':
            list_blockchains()

        elif choice == '4':
            if current_blockchain:
                new_block_data = input("Введите данные для нового блока: ").strip()
                create_new_block(current_blockchain, new_block_data)
                console.print("[green]Новый блок успешно добавлен в блокчейн.[/green]")
            else:
                console.print("[red]Ошибка: Сначала загрузите блокчейн.[/red]")

        elif choice == '5':
            if current_blockchain:
                view_blocks(current_blockchain)
            else:
                console.print("[red]Ошибка: Сначала загрузите блокчейн.[/red]")

        elif choice == '6':
            run_tests()

        elif choice == '7':
            update_project()

        elif choice == 'H':
            display_help_menu()

        elif choice == 'Q':
            console.print("Выход...")
            break

        else:
            console.print("[red]Неверный выбор. Попробуйте снова.[/red]")

def blockchain_exists(blockchain_name):
    """
    Проверяет, существует ли блокчейн с данным именем.
    """
    blockchain_file = f"{os.path.join(BLOCKCHAIN_DIR, hashlib.sha256(blockchain_name.encode()).hexdigest())}.json"
    return os.path.exists(blockchain_file)


if __name__ == "__main__":
    main()
