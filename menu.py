# menu.py
# Меню pyChainLite
import os
import json
from rich.console import Console
from modules.blockchain_creation import create_blockchain
from modules.blockchain_loading import load_blockchain
from modules.block_creation import create_new_block
from modules.block_viewer import view_blocks
from modules.blockchain_listing import list_blockchains
from modules.update_project import update_project

console = Console()
current_blockchain = None

def main():
    while True:
        console.print("\nМеню pyChainLite\n1. Создать новый блокчейн\n2. Загрузить блокчейн\n3. Создать новый блок\n4. Просмотреть блоки\n5. Список блокчейнов\n6. Обновить проект\n7. Выйти")
        choice = input("Выберите действие (1-7): ")

        if choice == '1':
            create_blockchain()
        elif choice == '2':
            global current_blockchain
            current_blockchain = load_blockchain()
        elif choice == '3':
            create_new_block(current_blockchain)
        elif choice == '4':
            view_blocks(current_blockchain)
        elif choice == '5':
            list_blockchains()
        elif choice == '6':
            update_project()
        elif choice == '7':
            console.print("Выход...")
            break

if __name__ == "__main__":
    main()
