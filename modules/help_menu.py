# modules/help_menu.py
# Модуль для отображения меню помощи

from rich.console import Console
from rich.table import Table

console = Console()

def display_help_menu():
    """
    Отображение меню помощи.
    """
    table = Table(title="Меню помощи pyChainLite", show_header=True, header_style="bold green")
    table.add_column("##", style="dim")
    table.add_column("Описание", style="bold")

    table.add_row("1", "Описание функционала создания нового блокчейна")
    table.add_row("2", "Описание функционала загрузки блокчейна")
    table.add_row("3", "Описание функционала создания нового блока")
    table.add_row("4", "Описание функционала просмотра блоков")
    table.add_row("5", "Описание функционала списка блокчейнов")
    table.add_row("6", "Описание функционала запуска тестов")
    table.add_row("7", "Описание функционала обновления проекта")
    table.add_row("Q", "Выход из меню помощи")

    console.print(table)
