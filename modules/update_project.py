# modules/update_project.py
# Модуль для обновления проекта pyChainLite

import subprocess

def is_git_repo():
    """
    Проверяет, находится ли текущая директория в git-репозитории.
    """
    try:
        subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False

def reset_local_changes():
    """
    Выполняет сброс локальных изменений с предупреждением для пользователя.
    """
    print("⚠ Внимание: Выполнение 'git reset --hard HEAD' приведет к потере всех незакоммиченных изменений.")
    choice = input("Продолжить? (y/n): ").strip().lower()
    if choice == 'y':
        try:
            subprocess.run(["git", "reset", "--hard", "HEAD"], check=True)
            print("Локальные изменения сброшены.")
        except subprocess.CalledProcessError as e:
            print(f"Ошибка: не удалось сбросить изменения. {e}")
            return False
        return True
    else:
        print("Сброс изменений отменён.")
        return False

def update_project():
    """
    Выполняет обновление проекта через 'git pull'.
    """
    if not is_git_repo():
        print("Не найден Git-репозиторий. Пропускаем принудительное обновление.")
        return
    
    try:
        print("Принудительное обновление проекта...")
        # Пробуем обновить проект
        subprocess.run(["git", "pull"], check=True)
        print("Проект успешно обновлён!")
    except subprocess.CalledProcessError as e:
        # Если ошибка из-за локальных изменений
        if "локальные изменения будут перезаписаны" in str(e):
            print("Обнаружены локальные изменения, которые могут быть перезаписаны.")
            if reset_local_changes():
                # После сброса изменений повторяем обновление
                try:
                    subprocess.run(["git", "pull"], check=True)
                    print("Проект успешно обновлён!")
                except subprocess.CalledProcessError as e:
                    print(f"Ошибка при повторном обновлении проекта: {e}")
            else:
                print("Принудительное обновление отменено.")
        else:
            print(f"Ошибка при обновлении проекта: {e}")

if __name__ == "__main__":
    update_project()
#
