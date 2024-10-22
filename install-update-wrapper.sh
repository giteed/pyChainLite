#!/bin/bash
# install-update-wrapper.sh
## Этот скрипт копирует install-update.sh в родительскую папку и запускает его оттуда.

# Получаем текущий путь к директории проекта (там, где находится этот скрипт)
PROJECT_DIR=$(dirname "$(realpath "$0")")

# Определяем путь к install-update.sh
INSTALL_SCRIPT="$PROJECT_DIR/install-update.sh"

# Проверяем, существует ли файл install-update.sh
if [ ! -f "$INSTALL_SCRIPT" ]; then
    echo "Ошибка: Файл install-update.sh не найден в директории проекта."
    exit 1
fi

# Определяем путь к родительской директории
PARENT_DIR=$(dirname "$PROJECT_DIR")

# Копируем install-update.sh в родительскую папку
cp "$INSTALL_SCRIPT" "$PARENT_DIR" || { echo "Ошибка при копировании install-update.sh в родительскую папку."; exit 1; }

# Делаем скрипт исполняемым
chmod +x "$PARENT_DIR/install-update.sh" || { echo "Ошибка при установке прав на выполнение для install-update.sh."; exit 1; }

# Переходим в родительскую папку
cd "$PARENT_DIR" || { echo "Ошибка: не удается перейти в родительскую папку."; exit 1; }

# Запускаем install-update.sh из родительской папки
./install-update.sh || { echo "Ошибка: не удалось запустить install-update.sh"; exit 1; }
