#!/bin/bash
# update-and-start.sh

# Получаем путь к директории скрипта
SCRIPT_DIR=$(dirname "$(realpath "$0")")

# Перемещаемся в родительскую директорию
cd .. || { echo "Ошибка: не удается выйти за директорию проекта."; exit 1; }

# Копируем файл install-update.sh в родительскую папку и задаем права на выполнение
if [ -f "$SCRIPT_DIR/install-update.sh" ]; then
    cp "$SCRIPT_DIR/install-update.sh" ../ || { echo "Ошибка: не удалось скопировать install-update.sh."; exit 1; }
    chmod +x ../install-update.sh || { echo "Ошибка: не удалось установить права на выполнение для install-update.sh."; exit 1; }
else
    echo "Ошибка: Файл install-update.sh не найден в папке проекта."
    exit 1
fi

# Запускаем install-update.sh из родительской папки
cd .. || { echo "Ошибка: не удается выйти в родительскую директорию."; exit 1; }
./install-update.sh || { echo "Ошибка: не удалось запустить install-update.sh"; exit 1; }

# Возвращаемся в папку проекта
cd "$SCRIPT_DIR" || { echo "Ошибка: не удается зайти в директорию проекта."; exit 1; }

# Запускаем скрипт start.sh
./start.sh || { echo "Ошибка: не удалось запустить start.sh"; exit 1; }

# Проверяем наличие алиаса upstart и выводим сообщение
if grep -q "alias upstart=" ~/.bashrc; then
    echo "Для быстрого запуска проекта можно использовать команду 'upstart' из любого места."
fi
