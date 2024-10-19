import os
import subprocess
import json
import hashlib
from rich.console import Console
from rich.table import Table
from src.blockchain import Block

console = Console()

# Папка для хранения блокчейнов
BLOCKCHAIN_DIR = "blockchains"

# Инициализируем список блокчейнов
current_blockchain = None

# Функция для создания хеша
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Функция для создания нового блокчейна
def create_blockchain():
    blockchain_name = input("Введите имя для нового блокчейна: ").strip()
    if not blockchain_name:
        console.print("[red]Имя блокчейна не может быть пустым.[/red]")
        return
    
    blockchain_owner = input("Введите имя владельца блокчейна: ").strip()
    if not blockchain_owner:
        console.print("[red]Имя владельца блокчейна не может быть пустым.[/red]")
        return

    owner_password = input("Введите пароль для владельца блокчейна: ").strip()
    if not owner_password:
        console.print("[red]Пароль не может быть пустым.[/red]")
        return

    hashed_password = hash_password(owner_password)
    
    blockchain_hash = hashlib.sha256(blockchain_name.encode()).hexdigest()
    blockchain_file = f"{blockchain_hash}.json"
    blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)

    if os.path.exists(blockchain_path):
        console.print(f"[red]Блокчейн с именем '{blockchain_name}' уже существует.[/red]")
        return

    # Создание директории, если она не существует
    os.makedirs(BLOCKCHAIN_DIR, exist_ok=True)

    # Создание генезис-блока с хешем имени блокчейна и паролем владельца
    genesis_block = Block(0, {"blockchain_name": blockchain_name, "owner": blockchain_owner, "owner_password_hash": hashed_password}, "0" * 64)

    # Сохранение блокчейна в файл
    blockchain_data = {"blocks": [genesis_block.__dict__]}
    with open(blockchain_path, 'w') as f:
        json.dump(blockchain_data, f, indent=4)

    console.print(f"\nБлокчейн '{blockchain_name}' успешно создан.")
    console.print(json.dumps(blockchain_data, indent=4))

# Функция для загрузки существующего блокчейна
def load_blockchain():
    blockchain_name = input("Введите имя блокчейна для загрузки: ").strip()
    if not blockchain_name:
        console.print("[red]Имя блокчейна не может быть пустым.[/red]")
        return
    
    blockchain_hash = hashlib.sha256(blockchain_name.encode()).hexdigest()
    blockchain_file = f"{blockchain_hash}.json"
    blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)

    if not os.path.exists(blockchain_path):
        console.print(f"[red]Блокчейн с именем '{blockchain_name}' не найден.[/red]")
        return
    
    with open(blockchain_path, 'r') as f:
        blockchain_data = json.load(f)

    console.print(f"\nБлокчейн '{blockchain_name}' загружен.")
    console.print(json.dumps(blockchain_data, indent=4))

    global current_blockchain
    current_blockchain = blockchain_data
    current_blockchain["file"] = blockchain_file

# Функция для вывода списка блокчейнов
def list_blockchains():
    if not os.path.exists(BLOCKCHAIN_DIR):
        console.print("[red]Папка с блокчейнами не найдена.[/red]")
        return

    blockchains = []
    for filename in os.listdir(BLOCKCHAIN_DIR):
        if filename.endswith(".json"):
            blockchain_path = os.path.join(BLOCKCHAIN_DIR, filename)
            with open(blockchain_path, 'r') as f:
                blockchain_data = json.load(f)
                genesis_block = blockchain_data["blocks"][0]
                blockchain_name = genesis_block["data"]["blockchain_name"]
                owner = genesis_block["data"]["owner"]
                hash_genesis = genesis_block["hash"]
                blockchains.append((filename, blockchain_name, owner, hash_genesis))

    if not blockchains:
        console.print("[yellow]Нет созданных блокчейнов.[/yellow]")
        return

    table = Table(title="Список блокчейнов", show_header=True, header_style="bold cyan")
    table.add_column("Имя файла блокчейна", style="dim")
    table.add_column("Имя блокчейна", style="bold")
    table.add_column("Владелец", style="bold")
    table.add_column("Хеш генезис-блока", style="bold")

    for blockchain in blockchains:
        table.add_row(blockchain[0], blockchain[1], blockchain[2], blockchain[3])

    console.print(table)

# Функция для запуска тестов
def run_tests():
    console.print("🧪 [bold magenta]Запуск тестов...[/bold magenta]")
    # Устанавливаем PYTHONPATH для тестов
    env = os.environ.copy()
    env['PYTHONPATH'] = os.path.join(os.getcwd(), "src")
    try:
        subprocess.run(['pytest'], check=True, env=env)
    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]Ошибка при запуске тестов: {e}[/bold red]")

# Функция для обновления проекта
def update_project():
    console.print("🔄 [bold cyan]Запуск обновления проекта...[/bold cyan]")
    subprocess.run(['chmod', '+x', './install-update.sh'], check=True)
    subprocess.run(['./install-update.sh'], check=True)

# Основное меню
def display_menu():
    table = Table(title="Меню pyChainLite", show_header=True, header_style="bold cyan")
    table.add_column("Номер", style="dim")
    table.add_column("Действие", style="bold")
    
    table.add_row("1", "Создать новый блокчейн")
    table.add_row("2", "Загрузить существующий блокчейн")
    table.add_row("3", "Просмотреть блоки текущего блокчейна")
    table.add_row("4", "Запустить тесты")
    table.add_row("5", "Показать список блокчейнов")
    table.add_row("6", "Обновить проект")
    table.add_row("7", "Выйти")

    console.print(table)

# Основной цикл программы
def main():
    while True:
        display_menu()
        choice = input("Выберите действие (1-7): ").strip()
        
        if choice == '1':
            create_blockchain()
        elif choice == '2':
            load_blockchain()
        elif choice == '3':
            if current_blockchain:
                console.print(json.dumps(current_blockchain, indent=4))
            else:
                console.print("[bold red]Сначала загрузите блокчейн.[/bold red]")
        elif choice == '4':
            run_tests()
        elif choice == '5':
            list_blockchains()
        elif choice == '6':
            update_project()
        elif choice == '7':
            console.print("[bold green]Выход...[/bold green]")
            break
        else:
            console.print("[bold red]Неверный выбор. Пожалуйста, выберите действие от 1 до 7.[/bold red]")

if __name__ == "__main__":
    main()
