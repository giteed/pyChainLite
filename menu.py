import os
import subprocess
from rich.console import Console
from rich.table import Table
from src.blockchain import Block

console = Console()

# Инициализируем первый блок (генезис блок)
blockchain = []

def display_menu():
    table = Table(title="Меню pyChainLite", show_header=True, header_style="bold cyan")
    table.add_column("Номер", style="dim")
    table.add_column("Действие", style="bold")
    
    table.add_row("1", "Запустить блокчейн")
    table.add_row("2", "Добавить новый блок")
    table.add_row("3", "Просмотреть блоки")
    table.add_row("4", "Запустить тесты")
    table.add_row("5", "Проверить/Создать алиас upstart")
    table.add_row("6", "Обновить проект")
    table.add_row("7", "Выйти")

    console.print(table)

def run_blockchain():
    console.print("🚀 [bold green]Запуск блокчейна...[/bold green]")
    # Создание генезис блока
    genesis_block = Block(0, "Генезис блок", "0" * 64)
    blockchain.append(genesis_block)
    console.print(f"Создан генезис блок: {genesis_block}")

def add_new_block():
    if not blockchain:
        console.print("[bold red]Блокчейн ещё не запущен. Запустите блокчейн сначала.[/bold red]")
        return

    # Получаем данные для нового блока
    data = input("Введите данные для нового блока: ")
    last_block = blockchain[-1]
    new_block = Block(last_block.index + 1, data, last_block.hash)
    blockchain.append(new_block)
    console.print(f"Добавлен новый блок: {new_block}")

def view_blocks():
    if not blockchain:
        console.print("[bold red]Блокчейн ещё не запущен.[/bold red]")
        return

    console.print("[bold blue]Текущие блоки в блокчейне:[/bold blue]")
    for block in blockchain:
        console.print(block)

def run_tests():
    console.print("🧪 [bold magenta]Запуск тестов...[/bold magenta]")
    # Устанавливаем PYTHONPATH для тестов
    env = os.environ.copy()
    env['PYTHONPATH'] = os.path.join(os.getcwd(), "src")
    try:
        subprocess.run(['pytest'], check=True, env=env)
    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]Ошибка при запуске тестов: {e}[/bold red]")

def check_alias():
    console.print("🔄 [bold yellow]Проверка алиаса upstart...[/bold yellow]")
    with open(os.path.expanduser("~/.bashrc"), "r") as file:
        bashrc_content = file.read()
    
    if "alias upstart=" in bashrc_content:
        console.print("[bold green]Алиас upstart уже существует.[/bold green]")
    else:
        console.print("[bold yellow]Алиас upstart не найден. Добавьте его вручную в ~/.bashrc.[/bold yellow]")

def update_project():
    console.print("🔄 [bold yellow]Запуск обновления проекта...[/bold yellow]")
    
    # Устанавливаем права на выполнение для install-update.sh
    if not os.access('./install-update.sh', os.X_OK):
        console.print("[bold yellow]Устанавливаю права на выполнение для install-update.sh[/bold yellow]")
        os.chmod('./install-update.sh', 0o755)

    try:
        # Запускаем скрипт обновления
        subprocess.run(['./install-update.sh'], check=True)
    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]Ошибка при обновлении проекта: {e}[/bold red]")

def main():
    while True:
        display_menu()
        choice = input("Выберите действие (1-7): ")
        
        if choice == '1':
            run_blockchain()
        elif choice == '2':
            add_new_block()
        elif choice == '3':
            view_blocks()
        elif choice == '4':
            run_tests()
        elif choice == '5':
            check_alias()
        elif choice == '6':
            update_project()
        elif choice == '7':
            console.print("[bold green]Выход...[/bold green]")
            break
        else:
            console.print("[bold red]Неверный выбор. Пожалуйста, выберите действие от 1 до 7.[/bold red]")

if __name__ == "__main__":
    main()
