import os
import json
import hashlib
import time
import subprocess
from rich.console import Console
from rich.table import Table

console = Console()

BLOCKCHAIN_DIR = "blockchains"
current_blockchain = None
current_blockchain_file = None

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index                        # Номер блока
        self.timestamp = time.time()              # Время создания блока
        self.data = data                          # Данные блока
        self.previous_hash = previous_hash        # Хеш предыдущего блока
        self.hash = self.calculate_hash()         # Хеш текущего блока

    def calculate_hash(self):
        """
        Вычисляет хеш блока на основе его данных.
        """
        block_data = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_data.encode()).hexdigest()

    @classmethod
    def from_dict(cls, block_data):
        """
        Создает объект Block из словаря (например, загруженного из JSON).
        """
        block = cls(block_data['index'], block_data['data'], block_data['previous_hash'])
        block.timestamp = block_data['timestamp']
        block.hash = block_data['hash']
        return block

    def __repr__(self):
        return (f"Block(index: {self.index}, timestamp: {self.timestamp}, "
                f"data: {self.data}, previous_hash: {self.previous_hash}, hash: {self.hash})")

class Blockchain:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.blocks = []

def create_new_blockchain():
    global current_blockchain, current_blockchain_file

    blockchain_name = input("Введите имя для нового блокчейна: ")
    blockchain_hash = hashlib.sha256(blockchain_name.encode()).hexdigest()
    blockchain_file = os.path.join(BLOCKCHAIN_DIR, f"{blockchain_hash}.json")

    # Проверяем, существует ли блокчейн с таким именем
    if os.path.exists(blockchain_file):
        console.print(f"[bold red]Ошибка: блокчейн с именем '{blockchain_name}' уже существует.[/bold red]")
        return

    owner = input("Введите имя владельца блокчейна: ")
    current_blockchain = Blockchain(blockchain_name, owner)
    genesis_block = Block(0, blockchain_name, "0" * 64)  # Генезис блок
    current_blockchain.blocks.append(genesis_block)

    # Сохраняем блокчейн в файл
    if not os.path.exists(BLOCKCHAIN_DIR):
        os.makedirs(BLOCKCHAIN_DIR)

    with open(blockchain_file, 'w') as file:
        json.dump({"blocks": [block.__dict__ for block in current_blockchain.blocks]}, file, indent=4)

    current_blockchain_file = blockchain_file
    console.print(f"[bold green]Блокчейн '{blockchain_name}' успешно создан.[/bold green]")

def load_blockchain():
    global current_blockchain, current_blockchain_file

    blockchain_name = input("Введите имя блокчейна для загрузки: ")
    blockchain_hash = hashlib.sha256(blockchain_name.encode()).hexdigest()
    blockchain_file = os.path.join(BLOCKCHAIN_DIR, f"{blockchain_hash}.json")

    # Проверяем, существует ли блокчейн
    if not os.path.exists(blockchain_file):
        console.print(f"[bold red]Ошибка: блокчейн с именем '{blockchain_name}' не найден.[/bold red]")
        return

    # Загружаем блокчейн из файла
    with open(blockchain_file, 'r') as file:
        blockchain_data = json.load(file)
        current_blockchain = Blockchain(blockchain_name, "")
        current_blockchain.blocks = [Block.from_dict(block) for block in blockchain_data["blocks"]]
        current_blockchain_file = blockchain_file

    console.print(f"[bold green]Блокчейн '{blockchain_name}' загружен.[/bold green]")

def view_blocks():
    if not current_blockchain:
        console.print("[bold red]Блокчейн не загружен или не создан.[/bold red]")
        return

    console.print("[bold blue]Текущие блоки в блокчейне:[/bold blue]")
    for block in current_blockchain.blocks:
        console.print(block)

def add_new_block():
    if not current_blockchain:
        console.print("[bold red]Блокчейн не загружен или не создан.[/bold red]")
        return

    data = input("Введите данные для нового блока: ")
    last_block = current_blockchain.blocks[-1]
    new_block = Block(last_block.index + 1, data, last_block.hash)
    current_blockchain.blocks.append(new_block)

    # Сохраняем изменения в блокчейне
    with open(current_blockchain_file, 'w') as file:
        json.dump({"blocks": [block.__dict__ for block in current_blockchain.blocks]}, file, indent=4)

    console.print(f"[bold green]Новый блок добавлен в блокчейн '{current_blockchain.name}'.[/bold green]")

def run_tests():
    console.print("🧪 [bold magenta]Запуск тестов...[/bold magenta]")
    try:
        subprocess.run(['pytest'], check=True)
    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]Ошибка при запуске тестов: {e}[/bold red]")

def display_menu():
    table = Table(title="Меню pyChainLite", show_header=True, header_style="bold cyan")
    table.add_column("Номер", style="dim")
    table.add_column("Действие", style="bold")

    table.add_row("1", "Создать новый блокчейн")
    table.add_row("2", "Загрузить блокчейн")
    table.add_row("3", "Просмотреть блоки")
    table.add_row("4", "Добавить новый блок")
    table.add_row("5", "Запустить тесты")
    table.add_row("6", "Выйти")

    console.print(table)

def main():
    while True:
        display_menu()
        choice = input("Выберите действие (1-6): ")

        if choice == '1':
            create_new_blockchain()
        elif choice == '2':
            load_blockchain()
        elif choice == '3':
            view_blocks()
        elif choice == '4':
            add_new_block()
        elif choice == '5':
            run_tests()
        elif choice == '6':
            console.print("[bold green]Выход...[/bold green]")
            break
        else:
            console.print("[bold red]Неверный выбор. Пожалуйста, выберите действие от 1 до 6.[/bold red]")

if __name__ == "__main__":
    main()
