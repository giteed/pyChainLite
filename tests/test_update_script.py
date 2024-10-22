# tests/test_update_script.py
# Тест для скрипта обновления проекта pyChainLite
# Этот тест проверяет корректную работу скрипта обновления, включая принудительное обновление через git и запуск основного проекта.
# Скрипт запускается через subprocess, и проверяются ключевые сообщения в его выводе.

import subprocess
import os

def test_update_script():
    # Определяем путь к скрипту
    script_path = os.path.abspath("path/to/your/update-script.sh")

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
