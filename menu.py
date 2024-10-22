# menu.py
## Главное меню для взаимодействия с pyChainLite

import os
import sys
import hashlib
from rich.console import Console
from modules.blockchain_creation import create_blockchain
from modules.blockchain_loading import load_blockchain
from modules.block_viewer import view_blocks
from modules.block_creation import create_new_block
from modules.blockchain_listing import list_blockchains
from modules.run_tests import run_tests
from modules.update_project import update_project
from modules.menu_help import display_help_menu
from modules.debug import enable_debug, disable_debug

console = Console()

BLOCKCHAIN_DIR = "blockchains"
current_blockchain = None
debug_mode = False  # Добавляем глобальный параметр для режима отладки

def main():
    global current_blockchain, debug_mode

    while True:
        console.print(f"\n[bold]Текущий блокчейн:[/bold] [cyan]{current_blockchain['name'] if current_blockchain else 'Блокчейн не загружен'}[/cyan]\n")
        console.print(f"[bold]Режим отладки:[/bold] {'Включен' if debug_mode else 'Выключен'}\n")
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
            │ 8  │ 🛠️  Отладка Вкл/Выкл       │
            │ H  │ ❓ Описание функционала   │
            │    │                           │
            │ Q  │ 🚪 Выйти                  │
            └────┴───────────────────────────┘
        """)

        choice = input("Введите ваш выбор: ").strip().upper()

        if choice == '1':
            blockchain_name = input("Введите имя нового блокчейна: ").strip()
            if blockchain_exists(blockchain_name):
                console.print(f"[red]Блокчейн с именем '{blockchain_name}' уже существует. Операция прервана.[/red]")
            else:
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
                block_data = input("Введите данные для нового блока: ").strip()
                create_new_block(current_blockchain, block_data, "user_id")
                console.print("[green]Новый блок успешно добавлен в блокчейн.[/green]")
            else:
                console.print("[red]Ошибка: Блокчейн не загружен.[/red]")

        elif choice == '5':
            if current_blockchain:
                view_blocks(current_blockchain)
            else:
                console.print("[red]Ошибка: Блокчейн не загружен.[/red]")

        elif choice == '6':
            run_tests()

        elif choice == '7':
            update_project()

        elif choice == '8':  # Включить/выключить режим отладки
            if debug_mode:
                disable_debug()
                debug_mode = False
                console.print("[yellow]Режим отладки выключен.[/yellow]")
            else:
                enable_debug()
                debug_mode = True
                console.print("[green]Режим отладки включен.[/green]")

        elif choice == 'H':
            display_help_menu()

        elif choice == 'Q':
            console.print("Выход...")
            sys.exit()

        else:
            console.print("[red]Неверный выбор. Попробуйте снова.[/red]")


def blockchain_exists(blockchain_name):
    blockchain_file = f"{os.path.join(BLOCKCHAIN_DIR, hashlib.sha256(blockchain_name.encode()).hexdigest())}.json"
    return os.path.exists(blockchain_file)

if __name__ == "__main__":
    main()
