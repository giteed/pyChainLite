# tests/test_update_script.py
# Тест для скрипта обновления проекта pyChainLite
# Этот тест проверяет корректную работу скрипта обновления, включая принудительное обновление через git и запуск основного проекта.
# Скрипт запускается через subprocess, и проверяются ключевые сообщения в его выводе.

import subprocess
import os

def test_update_script():
    # Указываем путь к скрипту обновления в корневой папке проекта
    script_path = os.path.abspath("../install-update.sh")  # Убедитесь, что путь корректен для вашего скрипта

    # Проверяем, существует ли файл скрипта
    assert os.path.exists(script_path), f"Скрипт {script_path} не найден"

    # Выполняем скрипт и перехватываем вывод
    result = subprocess.run([script_path], capture_output=True, text=True)

    # Проверяем, что скрипт завершился успешно
    assert result.returncode == 0, f"Скрипт завершился с ошибкой: {result.stderr}"

    # Проверяем, что в выводе присутствуют важные части
    assert "Обновление существующего проекта..." in result.stdout, "Ожидаемый текст об обновлении не найден"
    assert "Проект успешно обновлен." in result.stdout, "Сообщение об успешном обновлении не найдено"

    # Проверяем наличие алиаса 'upstart' в .bashrc
    if "upstart" in result.stdout:
        assert "Для быстрого запуска проекта можно использовать команду 'upstart'" in result.stdout, "Ожидаемое сообщение об алиасе отсутствует"
    else:
        print("Алиас 'upstart' не найден в системе, шаг пропущен.")

    # Выводим результат теста
    print(result.stdout)

if __name__ == "__main__":
    test_update_script()
