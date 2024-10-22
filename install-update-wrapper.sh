#!/bin/bash
# install-update-wrapper.sh
# Скрипт для копирования install-update.sh и его запуска из родительской директории

# Получаем путь к директории, где находится этот скрипт
SCRIPT_DIR=$(dirname "$(realpath "$0")")

# Проверяем, существует ли файл install-update.sh в папке проекта
if [ -f "$SCRIPT_DIR/pyChainLite/install-update.sh" ]; then
    # Копируем файл install-update.sh в родительскую директорию
    cp "$SCRIPT_DIR/pyChainLite/install-update.sh" "$SCRIPT_DIR/.." || { echo "Ошибка: не удалось скопировать install-update.sh."; exit 1; }
    
    # Устанавливаем права на выполнение скрипта
    chmod +x "$SCRIPT_DIR/../install-update.sh" || { echo "Ошибка: не удалось установить права на выполнение для install-update.sh."; exit 1; }

    # Переходим в родительскую директорию и запускаем install-update.sh
    cd "$SCRIPT_DIR/.." || { echo "Ошибка: не удалось выйти в родительскую директорию."; exit 1; }
    ./install-update.sh || { echo "Ошибка: не удалось запустить install-update.sh"; exit 1; }
else
    echo "Ошибка: Файл install-update.sh не найден в директории проекта."
    exit 1
fi
