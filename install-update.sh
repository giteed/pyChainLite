#!/bin/bash

# Получаем путь к директории скрипта
SCRIPT_DIR=$(dirname "$(realpath "$0")")

# Перемещаемся в директорию скрипта
cd "$SCRIPT_DIR" || { echo "Ошибка: не удается зайти в директорию проекта."; exit 1; }

# Устанавливаем права на выполнение для install-update.sh
chmod +x ./install-update.sh || { echo "Ошибка: не удалось установить права на выполнение для install-update.sh"; exit 1; }

# Запускаем обновление
./install-update.sh || { echo "Ошибка: не удалось запустить install-update.sh"; exit 1; }

# Возвращаемся в папку проекта
cd "$SCRIPT_DIR" || { echo "Ошибка: не удается зайти в директорию проекта."; exit 1; }

# Запускаем скрипт start.sh
chmod +x ./start.sh || { echo "Ошибка: не удалось установить права на выполнение для start.sh"; exit 1; }
./start.sh || { echo "Ошибка: не удалось запустить start.sh"; exit 1; }

# Проверяем наличие алиаса upstart и выводим сообщение
if grep -q "alias upstart=" ~/.bashrc; then
    echo "Для быстрого запуска проекта можно использовать команду 'upstart' из любого места."
fi
