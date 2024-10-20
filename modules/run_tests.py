# modules/run_tests.py

import subprocess
from rich.console import Console

console = Console()

def run_tests():
    console.print("🧪 [bold magenta]Запуск тестов...[/bold magenta]")
    try:
        subprocess.run(['pytest'], check=True)
    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]Ошибка при запуске тестов: {e}[/bold red]")
