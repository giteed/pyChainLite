# modules/update_project.py
# Модуль для обновления проекта
import subprocess
import shutil
from rich.console import Console

console = Console()

def update_project():
    console.print("🔄 [bold cyan]Запуск обновления проекта...[/bold cyan]")
    subprocess.run(['chmod', '+x', './install-update.sh'], check=True)
    shutil.copy('./install-update.sh', '../install-update.sh')
    subprocess.run(['../install-update.sh'], check=True)
