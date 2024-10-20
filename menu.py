# menu.py
# Главное меню для управления pyChainLite

from rich.console import Console
from modules.blockchain_creation import create_blockchain
from modules.blockchain_loading import load_blockchain
from modules.blockchain_listing import list_blockchains  # Правильный импорт
from modules.block_creation import create_new_block
from modules.update_project import update_project
from modules.run_tests import run_tests
from modules.menu_help import show_help

console = Console()

def main():
    current_blockchain = None

    while True:
        console.print(f"\n[bold]Текущий блокчейн:[/bold] [cyan]{current_blockchain['name'] if current_blockchain else 'Блокчейн не загружен'}[/cyan]")

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

        choice = input("Введите ваш выбор: ").lower()

        if choice == "1":
            blockchain_name = input("Введите имя нового блокчейна: ")
            owner_name = input("Введите имя владельца: ")
            current_blockchain = create_blockchain(blockchain_name, owner_name)
            console.print(f"Блокчейн '{blockchain_name}' успешно создан.")
        
        elif choice == "2":
            blockchain_name = input("Введите имя блокчейна для загрузки: ")
            current_blockchain = load_blockchain(blockchain_name)
            if current_blockchain:
                console.print(f"Блокчейн '{blockchain_name}' успешно загружен.")
            else:
                console.print("[bold red]Ошибка: Блокчейн не найден.[/bold red]")
        
        elif choice == "3":
            list_blockchains()  # Вывод списка блокчейнов
        
        elif choice == "4":
            if current_blockchain:
                data = input("Введите данные для нового блока: ")
                create_new_block(current_blockchain, data)
            else:
                console.print("[bold red]Ошибка: Блокчейн не загружен.[/bold red]")
        
        elif choice == "5":
            if current_blockchain:
                console.print(f"Просмотр блоков в блокчейне '{current_blockchain['name']}':")
                for block in current_blockchain['blocks']:
                    console.print(block)
            else:
                console.print("[bold red]Ошибка: Блокчейн не загружен.[/bold red]")
        
        elif choice == "6":
            run_tests()
        
        elif choice == "7":
            update_project()
        
        elif choice == "h":
            show_help()  # Показываем справку
        
        elif choice == "q":
            console.print("Выход из программы...")
            break

if __name__ == "__main__":
    main()
