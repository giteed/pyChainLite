# modules/update_project.py
# Модуль для обновления проекта pyChainLite

import subprocess

def update_project():
    try:
        # Выполняем команду git pull
        subprocess.run(["git", "pull"], check=True)
        print("Проект успешно обновлён.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при обновлении проекта: {e}")

if __name__ == "__main__":
    update_project()
