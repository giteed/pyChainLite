import os
import subprocess
from rich.console import Console
from rich.table import Table

console = Console()

def display_menu():
    table = Table(title="Меню pyChainLite", show_header=True, header_style="bold cyan")
    table.add_column("Номер", style="dim")
    table.add_column("Действие", style="bold")
    
    table.add_row("1", "Запустить блокчейн")
    table.add_row("2", "Авторизация пользователя")
    table.add_row("3", "Просмотреть логи")
    table.add_row("4", "Запустить тесты")
    table.add_row("5", "Выйти")

    console.print(table)

def run_blockchain():
    console.print("🚀 [bold green]Запуск блокчейна...[/bold green]")
    # Здесь будет код для запуска блокчейна
    # Например, subprocess.call(['python', 'blockchain.py'])

def user_authorization():
    console.print("🔑 [bold yellow]Авторизация пользователя...[/bold yellow]")
    # Здесь будет код для авторизации пользователя
    # Например, subprocess.call(['python', 'auth.py'])

def view_logs():
    console.print("📄 [bold blue]Открытие логов...[/bold blue]")
    # Открытие логов
    log_file = os.path.join("logs", "install-update.log")
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            console.print(f.read())
    else:
        console.print("[bold red]Логи не найдены.[/bold red]")

def run_tests():
    console.print("🧪 [bold magenta]Запуск тестов...[/bold magenta]")
    # Запуск тестов через pytest
    try:
        subprocess.run(['pytest'], check=True)
    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]Ошибка при запуске тестов: {e}[/bold red]")

def main():
    while True:
        display_menu()
        choice = input("Выберите действие (1-5): ")
        
        if choice == '1':
            run_blockchain()
        elif choice == '2':
            user_authorization()
        elif choice == '3':
            view_logs()
        elif choice == '4':
            run_tests()
        elif choice == '5':
            console.print("[bold green]Выход...[/bold green]")
            break
        else:
            console.print("[bold red]Неверный выбор. Пожалуйста, выберите действие от 1 до 5.[/bold red]")

if __name__ == "__main__":
    main()
