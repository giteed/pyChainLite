# modules/update_project.py
# Модуль для обновления проекта и перезапуска меню

import os
import subprocess
import shutil

BLOCKCHAIN_DIR = "blockchains"

def update_project():
    """
    Функция для обновления проекта.
    """
    print("🔄 [bold cyan]Запуск обновления проекта...[/bold cyan]")
    
    # Устанавливаем права на выполнение для скрипта установки и обновления
    subprocess.run(['chmod', '+x', './install-update.sh'], check=True)
    
    # Перемещаем папку блокчейнов в родительский каталог для сохранности
    if os.path.exists(BLOCKCHAIN_DIR):
        parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
        backup_blockchain_dir = os.path.join(parent_dir, BLOCKCHAIN_DIR)
        shutil.move(BLOCKCHAIN_DIR, backup_blockchain_dir)
        print(f"[2024-10-20] Папка с блокчейнами временно перемещена в {backup_blockchain_dir}.")

    # Запускаем скрипт обновления
    subprocess.run(['./install-update.sh'], check=True)

    # Возвращаем папку с блокчейнами обратно в проект
    if os.path.exists(backup_blockchain_dir):
        shutil.move(backup_blockchain_dir, os.getcwd())
        print(f"[2024-10-20] Папка с блокчейнами успешно возвращена в проект.")

    # Перезапуск меню
    restart_menu()

def restart_menu():
    """
    Перезапуск скрипта menu.py
    """
    # Получаем путь к текущему скрипту
    script_path = os.path.join(os.getcwd(), 'menu.py')

    # Устанавливаем права на выполнение для скрипта menu.py
    subprocess.run(['chmod', '+x', script_path], check=True)

    # Запускаем новый процесс с menu.py и выходим из текущего
    os.execv(script_path, ['python3', script_path])
