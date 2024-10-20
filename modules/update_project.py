# modules/update_project.py
# Модуль для обновления проекта pyChainLite

import os
import subprocess
import shutil
from rich.console import Console

console = Console()

# Функция для обновления проекта
def update_project():
    console.print("🔄 [bold cyan]Запуск обновления проекта...[/bold cyan]")

    # Перемещаем папку с блокчейнами в родительский каталог
    blockchain_dir = os.path.join(os.getcwd(), "blockchains")
    parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
    backup_dir = os.path.join(parent_dir, "blockchains")

    if os.path.exists(blockchain_dir):
        shutil.move(blockchain_dir, backup_dir)
        console.print(f"[{get_current_time()}] Папка с блокчейнами временно перемещена в {backup_dir}.")
    
    # Проверка на наличие локальных изменений
    result = subprocess.run(['git', 'status', '--porcelain'], stdout=subprocess.PIPE)
    if result.stdout:
        console.print("[bold red]Внимание: У вас есть локальные изменения.[/bold red]")
        console.print("Вы хотите спрятать их и продолжить обновление? (y/n)")
        choice = input().lower()
        if choice == 'y':
            # Спрятать локальные изменения
            console.print("Сохранение ваших локальных изменений...")
            subprocess.run(['git', 'stash'], check=True)
        else:
            console.print("[bold yellow]Отмена обновления.[/bold yellow]")
            return

    # Выполняем обновление
    subprocess.run(['chmod', '+x', './install-update.sh'], check=True)
    try:
        result = subprocess.run(['git', 'pull', 'origin', 'main'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        console.print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]Ошибка обновления: {e}[/bold red]")
    
    # Возвращаем изменения из stash, если они были спрятаны
    stash_result = subprocess.run(['git', 'stash', 'list'], stdout=subprocess.PIPE)
    if stash_result.stdout:
        console.print("Возвращение ваших изменений...")
        subprocess.run(['git', 'stash', 'pop'], check=True)

    # Возвращаем папку с блокчейнами обратно в проект
    if os.path.exists(backup_dir):
        console.print("\nЖелаете переместить папку с блокчейнами обратно в проект? (Y/n)")
        choice = input().lower()
        if choice != 'n':
            shutil.move(backup_dir, blockchain_dir)
            console.print(f"[{get_current_time()}] Папка с блокчейнами успешно перемещена обратно в проект.")

    # Перезапуск меню после обновления
    restart_menu()

# Функция для получения текущего времени
def get_current_time():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Функция для перезапуска меню
def restart_menu():
    script_path = os.path.join(os.getcwd(), 'menu.py')

    # Устанавливаем права на выполнение скрипта
    os.chmod(script_path, 0o755)

    # Используем execv для замены текущего процесса на новый процесс Python, который перезапустит скрипт меню
    console.print("[bold green]Перезапуск меню...[/bold green]")
    os.execv('/usr/bin/python3', ['python3', script_path])
