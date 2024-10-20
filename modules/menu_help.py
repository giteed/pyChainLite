# modules/menu_help.py
# Описание функционала меню pyChainLite

import os
from rich.console import Console
from rich.table import Table

console = Console()

HELP_DIR = "doc/menu_help"

def display_help_menu():
    table = Table(title="ℹ️  Описание функционала", show_header=True, header_style="bold yellow")
    table.add_column("##", style="dim")
    table.add_column("Описание", style="bold")

    # Описание функционала по разделам
    table.add_row("1", "🧱 Создать новый блокчейн")
    table.add_row("2", "📂 Загрузить блокчейн")
    table.add_row("3", "📜 Список блокчейнов")
    table.add_row("4", "📝 Создать новый блок")
    table.add_row("5", "🔍 Просмотреть блоки")
    table.add_row("6", "🧪 Запустить тесты")
    table.add_row("7", "🔄 Обновить проект")
    table.add_row("Q", "🚪 Вернуться в основное меню")

    console.print(table)

    choice = input("Выберите пункт для справки (1-7 или Q): ").strip().upper()

    if choice == 'Q':
        return
    else:
        display_help_content(choice)

def display_help_content(choice):
    help_files = {
        '1': "1_create_blockchain.md",
        '2': "2_load_blockchain.md",
        '3': "3_list_blockchains.md",
        '4': "4_create_new_block.md",
        '5': "5_view_blocks.md",
        '6': "6_run_tests.md",
        '7': "7_update_project.md",
        'Q': None,
    }

    help_file = help_files.get(choice)
    if help_file:
        file_path = os.path.join(HELP_DIR, help_file)
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                content = f.read()
            console.print(content)
        else:
            console.print(f"[red]Файл с описанием '{help_file}' не найден.[/red]")
    else:
        console.print("[red]Неверный выбор.[/red]")

    input("\nНажмите Enter для возврата в меню помощи...")
