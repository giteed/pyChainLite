import os
import subprocess

def display_menu():
    print("Меню pyChainLite")
    print("1. Запустить блокчейн")
    print("2. Авторизация пользователя")
    print("3. Просмотреть логи")
    print("4. Запустить тесты")
    print("5. Выйти")

def run_blockchain():
    print("Запуск блокчейна...")
    # Здесь будет код для запуска блокчейна
    # Например, subprocess.call(['python', 'blockchain.py'])

def user_authorization():
    print("Авторизация пользователя...")
    # Здесь будет код для авторизации пользователя
    # Например, subprocess.call(['python', 'auth.py'])

def view_logs():
    print("Открытие логов...")
    # Открытие логов (например, через командную строку или редактор)
    log_file = os.path.join("logs", "install-update.log")
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            print(f.read())
    else:
        print("Логи не найдены.")

def run_tests():
    print("Запуск тестов...")
    # Запуск тестов через pytest
    try:
        subprocess.run(['pytest'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при запуске тестов: {e}")

def main():
    while True:
        display_menu()
        choice = input("Выберите действие (1-5): ")
        
        if choice == '1':
            run_blockchain()
        elif choice == '2':
            user_authorization()
        elif choice == '3':
            view_logs()
        elif choice == '4':
            run_tests()
        elif choice == '5':
            print("Выход...")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие от 1 до 5.")

if __name__ == "__main__":
    main()
