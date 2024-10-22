# tests/test_update_script.py
# Тест для скрипта обновления проекта pyChainLite
# Этот тест проверяет корректную работу скрипта обновления, включая принудительное обновление через git и запуск основного проекта.
# Скрипт запускается через subprocess, и проверяются ключевые сообщения в его выводе.

import subprocess
import os

def test_update_script():
    # Указываем путь к скрипту обновления в корневой папке проекта (скорее всего это install-update.sh)
    script_path = os.path.abspath("../install-update.sh")  # Измените на актуальное имя скрипта

    # Проверяем, существует ли файл скрипта
    assert os.path.exists(script_path), f"Скрипт {script_path} не найден"

    # Выполняем скрипт и перехватываем вывод
    result = subprocess.run([script_path], capture_output=True, text=True)

    # Проверяем, что скрипт завершился успешно
    assert result.returncode == 0, f"Скрипт завершился с ошибкой: {result.stderr}"

    # Проверяем, что в выводе присутствуют важные части
    assert "Принудительное обновление проекта..." in result.stdout, "Ожидаемый текст не найден"
    assert "Для быстрого запуска проекта можно использовать команду 'upstart'" in result.stdout, "Ожидаемое сообщение об алиасе отсутствует"

    # Выводим результат теста
    print(result.stdout)

if __name__ == "__main__":
    test_update_script()
