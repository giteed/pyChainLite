# modules/debug.py
# Модуль для управления отладочными сообщениями

from rich.console import Console

console = Console()
DEBUG_MODE = False  # Глобальный флаг для управления отладкой

def set_debug_mode(state: bool):
    """
    Устанавливает режим отладки.
    """
    global DEBUG_MODE
    DEBUG_MODE = state

def debug(message: str):
    """
    Выводит отладочное сообщение, если отладка включена.
    """
    if DEBUG_MODE:
        console.print(f"[blue]Отладка:[/blue] {message}")
