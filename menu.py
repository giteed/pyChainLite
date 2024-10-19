import os
import json
import hashlib
import time
from rich.console import Console
from rich.table import Table

console = Console()

# Директория для хранения блокчейнов
BLOCKCHAIN_DIR = "blockchains"

# Глобальная переменная для хранения текущего блокчейна
current_blockchain = None
current_blockchain_file = None

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_data.encode()).hexdigest()

    def __repr__(self):
        return (f"Block(index: {self.index}, timestamp: {self.timestamp}, "
                f"data: {self.data}, previous_hash: {self.previous_hash}, hash: {self.hash})")

class Blockchain:
    def __init__(self, name, genesis_data):
        self.name = name
        self.blocks = []
        genesis_block = Block(0, genesis_data, "0" * 64)
        self.blocks.append(genesis_block)

    def add_block(self, data):
        last_block = self.blocks[-1]
        new_block = Block(last_block.index + 1, data, last_block.hash)
        self.blocks.append(new_block)

    def save_to_file(self):
        with open(current_blockchain_file, 'w') as file:
            json.dump({"blocks": [block.__dict__ for block in self.blocks]}, file, indent=4)

def display_menu():
    table = Table(title="Меню pyChainLite", show_header=True, header_style="bold cyan")
    table.add_column("Номер", style="dim")
    table.add_column("Действие", style="bold")
    
    table.add_row("1", "Создать новый блокчейн")
    table.add_row("2", "Загрузить блокчейн")
    table.add_row("3", "Добавить блок")
    table.add_row("4", "Просмотреть блоки")
    table.add_row("5", "Выйти")
    
    console.print(table)

def create_blockchain():
    global current_blockchain, current_blockchain_file

    blockchain_name = input("Введите имя для нового блокчейна: ")
    blockchain_hash = hashlib.sha256(blockchain_name.encode()).hexdigest()
    blockchain_file = os.path.join(BLOCKCHAIN_DIR, f"{blockchain_hash}.json")

    # Проверяем, существует ли уже такой блокчейн
    if os.path.exists(blockchain_file):
        console.print(f"[bold red]Ошибка: блокчейн с именем '{blockchain_name}' уже существует.[/bold red]")
        return

    # Создаем новый блокчейн
    genesis_data = input("Введите данные для генезис блока: ")
    current_blockchain = Blockchain(blockchain_name, genesis_data)
    current_blockchain_file = blockchain_file

    # Сохраняем блокчейн в файл
    current_blockchain.save_to_file()
    console.print(f"[bold green]Новый блокчейн '{blockchain_name}' создан и сохранён как {blockchain_hash}.json.[/bold green]")

def load_blockchain():
    global current_blockchain, current_blockchain_file

    blockchain_name = input("Введите имя блокчейна для загрузки: ")
    blockchain_hash = hashlib.sha256(blockchain_name.encode()).hexdigest()
    blockchain_file = os.path.join(BLOCKCHAIN_DIR, f"{blockchain_hash}.json")

    # Проверяем, существует ли блокчейн
    if not os.path.exists(blockchain_file):
        console.print(f"[bold red]Ошибка: блокчейн с именем '{blockchain_name}' не найден.[/bold red]")
        return

    # Загружаем блокчейн
    with open(blockchain_file, 'r') as file:
        blockchain_data = json.load(file)
        current_blockchain = Blockchain(blockchain_name, "")
        current_blockchain.blocks = [Block(**block) for block in blockchain_data["blocks"]]
        current_blockchain_file = blockchain_file

    console.print(f"[bold green]Блокчейн '{blockchain_name}' загружен.[/bold green]")

def add_block():
    if current_blockchain is None:
        console.print("[bold red]Ошибка: сначала загрузите или создайте блокчейн.[/bold red]")
        return

    data = input("Введите данные для нового блока: ")
    current_blockchain.add_block(data)
    current_blockchain.save_to_file()
    console.print("[bold green]Новый блок добавлен в блокчейн.[/bold green]")

def view_blocks():
    if current_blockchain is None:
        console.print("[bold red]Ошибка: сначала загрузите или создайте блокчейн.[/bold red]")
        return

    console.print("[bold blue]Текущие блоки в блокчейне:[/bold blue]")
    for block in current_blockchain.blocks:
        console.print(block)

def main():
    while True:
        display_menu()
        choice = input("Выберите действие (1-5): ")
        
        if choice == '1':
            create_blockchain()
        elif choice == '2':
            load_blockchain()
        elif choice == '3':
            add_block()
        elif choice == '4':
            view_blocks()
        elif choice == '5':
            console.print("[bold green]Выход...[/bold green]")
            break
        else:
            console.print("[bold red]Неверный выбор. Пожалуйста, выберите действие от 1 до 5.[/bold red]")

if __name__ == "__main__":
    # Проверяем, существует ли директория для блокчейнов
    if not os.path.exists(BLOCKCHAIN_DIR):
        os.makedirs(BLOCKCHAIN_DIR)

    main()
