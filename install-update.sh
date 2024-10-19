#!/bin/bash

# Получаем путь к директории скрипта
SCRIPT_DIR=$(dirname "$(realpath "$0")")

# Определяем пути для папок проекта и логов
PROJECT_DIR="$SCRIPT_DIR/pyChainLite"
LOG_DIR="$PROJECT_DIR/logs"
LOG_FILE="$LOG_DIR/install-update.log"

# Проверяем существование папки проекта и создаем её при необходимости
if [ ! -d "$PROJECT_DIR" ]; then
    echo "Папка проекта не найдена. Создаю папку $PROJECT_DIR..."
    mkdir -p "$PROJECT_DIR" || { echo "Ошибка: не удалось создать папку проекта."; exit 1; }

    echo "Клонирование репозитория в папку $PROJECT_DIR..."
    git clone https://github.com/giteed/pyChainLite.git "$PROJECT_DIR" || { echo "Ошибка клонирования репозитория."; exit 1; }
    
    echo "Клонирование завершено успешно."
fi

# Переходим в папку проекта перед созданием директорий
cd "$PROJECT_DIR" || { echo "Ошибка: не удается зайти в директорию проекта."; exit 1; }

# Проверяем наличие файла create_dirs.sh
if [ ! -f "$PROJECT_DIR/create_dirs.sh" ]; then
    echo "Ошибка: скрипт create_dirs.sh не найден. Проверьте наличие файла в репозитории."
    exit 1
fi

# Запуск скрипта для создания папок src и tests
echo "Проверка и создание необходимых директорий..."
chmod +x "$PROJECT_DIR/create_dirs.sh"
"$PROJECT_DIR/create_dirs.sh"

# Если проект уже существует, выполняем обновление
if [ -d "$PROJECT_DIR/.git" ]; then
    echo "Проект уже существует, выполняется обновление..."
    cd "$PROJECT_DIR" || { echo "Ошибка: не удается зайти в директорию проекта."; exit 1; }

    # Принудительно сбрасываем изменения и обновляем проект
    echo "Сброс локальных изменений..."
    git reset --hard HEAD || { echo "Ошибка при сбросе изменений."; exit 1; }
    
    echo "Обновление репозитория..."
    git pull origin main || { echo "Ошибка при обновлении репозитория."; exit 1; }

    echo "Установка прав на выполнение для start.sh..."
    chmod +x "$PROJECT_DIR/start.sh" || { echo "Ошибка при установке прав на выполнение для start.sh."; exit 1; }
else
    echo "Клонирование репозитория в папку $PROJECT_DIR..."
    git clone https://github.com/giteed/pyChainLite.git "$PROJECT_DIR" || { echo "Ошибка клонирования репозитория."; exit 1; }
fi

# Перемещаемся в директорию проекта для установки зависимостей
cd "$PROJECT_DIR" || { echo "Ошибка: не удается зайти в директорию проекта."; exit 1; }

# Создаем виртуальное окружение, если оно не создано
if [ ! -d "venv" ]; then
    echo "Создание виртуального окружения..."
    python3 -m venv venv || { echo "Ошибка создания виртуального окружения."; exit 1; }
else
    echo "Виртуальное окружение уже существует."
fi

# Активация виртуального окружения
echo "Активация виртуального окружения..."
source venv/bin/activate || { echo "Ошибка активации виртуального окружения."; exit 1; }

# Установка зависимостей
if [ -f "$PROJECT_DIR/requirements.txt" ]; then
    echo "Установка зависимостей из requirements.txt..."
    pip install --upgrade pip || { echo "Ошибка обновления pip."; exit 1; }
    pip install -r requirements.txt || { echo "Ошибка установки зависимостей."; exit 1; }
else
    echo "Файл requirements.txt не найден. Установка зависимостей невозможна."
    exit 1
fi

echo "Установка или обновление завершены успешно."

# Добавляем алиас в ~/.bashrc для команды upstart
if ! grep -q "alias upstart=" ~/.bashrc; then
    echo "Добавляем алиас upstart в ~/.bashrc..."
    echo '# Алиас для быстрого запуска update-and-start.sh' >> ~/.bashrc
    echo "alias upstart='bash $PROJECT_DIR/update-and-start.sh'" >> ~/.bashrc
    echo "Алиас upstart успешно добавлен."
    source ~/.bashrc
else
    echo "Алиас upstart уже существует в ~/.bashrc."
fi

# Завершение работы виртуального окружения
deactivate
cd "$SCRIPT_DIR"

echo "Скрипт завершил работу. Лог записан в $LOG_FILE."
