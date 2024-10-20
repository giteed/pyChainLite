# modules/update_project.py
# Модуль для обновления проекта

import os
import subprocess
import shutil
from rich.console import Console

console = Console()

def update_project():
    console.print("🔄 [bold cyan]Запуск обновления проекта...[/bold cyan]")
    subprocess.run(['chmod', '+x', './install-update.sh'], check=True)
    
    # Копируем файл в родительский каталог
    shutil.copy('./install-update.sh', '../install-update.sh')
    
    # Переходим в родительский каталог
    os.chdir('..')

    # Запускаем перемещенный файл
    subprocess.run(['./install-update.sh'], check=True)

    # Предлагаем перезапустить меню после обновления
    console.print("[bold green]Проект обновлен. Перезапуск меню...[/bold green]")

    # Перезапускаем меню
    restart_menu()

def restart_menu():
    """
    Перезапуск скрипта menu.py
    """
    # Получаем путь к текущему скрипту
    script_path = os.path.join(os.getcwd(), 'pyChainLite', 'menu.py')

    # Запускаем новый процесс с menu.py и выходим из текущего
    os.execv(script_path, ['python3', script_path])
