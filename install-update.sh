#!/bin/bash

# Определяем абсолютный путь к текущей директории и к папкам проекта и логов
BASE_DIR=$(pwd)
PROJECT_DIR="$BASE_DIR/pyChainLite"
LOG_DIR="$PROJECT_DIR/logs"
LOG_FILE="$LOG_DIR/install-update.log"

# Функция для записи в лог с датой и временем
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Проверяем существование папки проекта
if [ ! -d "$PROJECT_DIR" ]; then
    log "Ошибка: папка проекта $PROJECT_DIR не существует. Выполните установку проекта сначала."
    exit 1
fi

# Создаем папку для логов внутри проекта, если она не существует
if [ ! -d "$LOG_DIR" ]; then
    log "Создание директории для логов..."
    mkdir -p "$LOG_DIR" || { log "Ошибка создания директории для логов."; exit 1; }
fi

# Создаем файл лога, если он не существует
if [ ! -f "$LOG_FILE" ]; then
    log "Создание файла лога..."
    touch "$LOG_FILE" || { log "Ошибка создания файла лога."; exit 1; }
fi

log "Запуск установки/обновления"

# Проверяем наличие Python
if ! command -v python3 &> /dev/null; then
    log "Python3 не установлен. Установите Python версии 3.12.x."
    exit 1
fi

log "Python установлен: $(python3 --version)"

# Проверяем наличие Git
if ! command -v git &> /dev/null; then
    log "Git не установлен. Установите Git для продолжения."
    exit 1
fi

log "Git установлен: $(git --version)"

# Запуск скрипта для создания папок src и tests
echo "Проверка и создание необходимых директорий..."
chmod +x create_dirs.sh
./create_dirs.sh

# Проверка, был ли проект уже клонирован
if [ ! -d "$PROJECT_DIR/.git" ]; then
    log "Клонирование репозитория в папку $PROJECT_DIR..."
    git clone https://github.com/giteed/pyChainLite.git "$PROJECT_DIR" || { log "Ошибка клонирования репозитория."; exit 1; }
    
    # Делаем start.sh исполняемым
    log "Установка прав на выполнение для start.sh..."
    chmod +x "$PROJECT_DIR/start.sh" || { log "Ошибка при установке прав на выполнение для start.sh."; exit 1; }
else
    log "Проект уже существует, выполняется обновление..."
    cd "$PROJECT_DIR" || { log "Ошибка: не удается зайти в директорию проекта."; exit 1; }

    # Принудительно сбрасываем изменения и обновляем проект
    log "Сброс локальных изменений..."
    git reset --hard HEAD || { log "Ошибка при сбросе изменений."; exit 1; }
    
    log "Обновление репозитория..."
    git pull origin main || { log "Ошибка при обновлении репозитория."; exit 1; }

    # Восстанавливаем start.sh, если он был удален
    if [ ! -f "start.sh" ]; then
        log "Файл start.sh был удалён локально, восстанавливаю его из репозитория..."
        git checkout origin/main -- start.sh || { log "Ошибка при восстановлении start.sh."; exit 1; }
    fi

    log "Установка прав на выполнение для start.sh..."
    chmod +x "start.sh" || { log "Ошибка при установке прав на выполнение для start.sh после обновления."; exit 1; }
    cd "$BASE_DIR"
fi

# Перемещаемся в директорию проекта для установки зависимостей
cd "$PROJECT_DIR" || { log "Ошибка: не удается зайти в директорию проекта."; exit 1; }

# Создаем виртуальное окружение, если оно не создано
if [ ! -d "venv" ]; then
    log "Создание виртуального окружения..."
    python3 -m venv venv || { log "Ошибка создания виртуального окружения."; exit 1; }
else
    log "Виртуальное окружение уже существует."
fi

# Активация виртуального окружения
log "Активация виртуального окружения..."
source venv/bin/activate || { log "Ошибка активации виртуального окружения."; exit 1; }

# Установка зависимостей
if [ -f "requirements.txt" ]; then
    log "Установка зависимостей из requirements.txt..."
    pip install --upgrade pip || { log "Ошибка обновления pip."; exit 1; }
    pip install -r requirements.txt || { log "Ошибка установки зависимостей."; exit 1; }
else
    log "Файл requirements.txt не найден. Установка зависимостей невозможна."
    exit 1
fi

log "Установка или обновление завершены успешно."

# Завершение работы виртуального окружения
deactivate
cd "$BASE_DIR"

log "Скрипт завершил работу. Лог записан в $LOG_FILE."
