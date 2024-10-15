from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

# Инициализация объекта для вывода в консоль
console = Console()

def display_menu():
    """Функция для отображения главного меню pyChainLite"""
    console.clear()

    # Создаем таблицу для красивого отображения меню
    table = Table(title="pyChainLite - Главное меню")

    table.add_column("Номер", justify="center", style="cyan", no_wrap=True)
    table.add_column("Операция", justify="left", style="magenta")

    # Добавляем пункты меню
    table.add_row("1", "Запустить блокчейн")
    table.add_row("2", "Авторизация пользователя")
    table.add_row("3", "Просмотреть логи")
    table.add_row("4", "Выход")

    console.print(table)

def handle_menu_choice():
    """Функция для обработки выбора пользователя"""
    while True:
        display_menu()
        choice = Prompt.ask("[bold yellow]Выберите действие (1-4)")

        if choice == "1":
            console.print("[bold green]Запуск блокчейна...[/bold green]")
            # Здесь будет код запуска блокчейна
        elif choice == "2":
            console.print("[bold green]Авторизация пользователя...[/bold green]")
            # Здесь будет код авторизации
        elif choice == "3":
            console.print("[bold green]Просмотр логов...[/bold green]")
            # Здесь будет код просмотра логов
        elif choice == "4":
            console.print("[bold red]Выход из программы...[/bold red]")
            break
        else:
            console.print("[bold red]Неверный выбор, попробуйте снова.[/bold red]")

if __name__ == "__main__":
    handle_menu_choice()
