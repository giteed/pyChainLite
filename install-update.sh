#!/bin/bash

# Получаем путь к директории скрипта
SCRIPT_DIR=$(dirname "$(realpath "$0")")

# Определяем путь для папки проекта pyChainLite
PROJECT_DIR="$SCRIPT_DIR/pyChainLite"
LOG_DIR="$PROJECT_DIR/logs"
LOG_FILE="$LOG_DIR/install-update.log"

# Функция для записи в лог с датой и временем
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Логирование начнется только после клонирования/обновления проекта
init_logging() {
    # Создаем папку для логов, если она не существует
    if [ ! -d "$LOG_DIR" ]; then
        mkdir -p "$LOG_DIR" || { echo "Ошибка создания директории для логов."; exit 1; }
    fi

    # Создаем файл лога, если он не существует
    if [ ! -f "$LOG_FILE" ]; then
        touch "$LOG_FILE" || { echo "Ошибка создания файла лога."; exit 1; }
    fi

    log "Запуск установки/обновления"
}

# Проверка наличия Python
if ! command -v python3 &> /dev/null; then
    echo "Python3 не установлен. Установите Python версии 3.12.x."
    exit 1
fi

# Проверка наличия Git
if ! command -v git &> /dev/null; then
    echo "Git не установлен. Установите Git для продолжения."
    exit 1
fi

# Если папка pyChainLite уже существует, обновляем проект
if [ -d "$PROJECT_DIR/.git" ]; then
    cd "$PROJECT_DIR" || { echo "Ошибка: не удается зайти в директорию проекта."; exit 1; }
    echo "Обновление существующего проекта..."
    git pull origin main || { echo "Ошибка при обновлении проекта. Проверьте наличие конфликтов."; exit 1; }
    echo "Проект успешно обновлен."
    init_logging
else
    # Если проект отсутствует, клонируем репозиторий
    echo "Клонирование проекта в текущую директорию..."
    git clone https://github.com/giteed/pyChainLite.git "$PROJECT_DIR" || { echo "Ошибка клонирования репозитория."; exit 1; }
    echo "Клонирование завершено успешно."
    init_logging
fi

# Переходим в папку проекта перед установкой
cd "$PROJECT_DIR" || { log "Ошибка: не удалось зайти в директорию проекта."; exit 1; }

# Установка прав на выполнение для start.sh и update-and-start.sh
log "Установка прав на выполнение для start.sh и update-and-start.sh..."
chmod +x "$PROJECT_DIR/start.sh" || { log "Ошибка при установке прав на выполнение для start.sh."; exit 1; }
chmod +x "$PROJECT_DIR/update-and-start.sh" || { log "Ошибка при установке прав на выполнение для update-and-start.sh."; exit 1; }

# Создание виртуального окружения, если оно не создано
if [ ! -d "$PROJECT_DIR/venv" ]; then
    log "Создание виртуального окружения..."
    python3 -m venv "$PROJECT_DIR/venv" || { log "Ошибка создания виртуального окружения."; exit 1; }
else
    log "Виртуальное окружение уже существует."
fi

# Активация виртуального окружения
log "Активация виртуального окружения..."
source "$PROJECT_DIR/venv/bin/activate" || { log "Ошибка активации виртуального окружения."; exit 1; }

# Установка зависимостей
if [ -f "$PROJECT_DIR/requirements.txt" ]; then
    log "Установка зависимостей из requirements.txt..."
    pip install --upgrade pip || { log "Ошибка обновления pip."; exit 1; }
    pip install -r "$PROJECT_DIR/requirements.txt" || { log "Ошибка установки зависимостей."; exit 1; }
else
    log "Файл requirements.txt не найден. Установка зависимостей невозможна."
    exit 1
fi

log "Установка или обновление завершены успешно."

# Добавление алиаса в ~/.bashrc для команды upstart
if ! grep -q "alias upstart=" ~/.bashrc; then
    log "Добавляем алиас upstart в ~/.bashrc..."
    echo '# Алиас для быстрого запуска update-and-start.sh' >> ~/.bashrc
    echo "alias upstart='bash $PROJECT_DIR/update-and-start.sh'" >> ~/.bashrc
    log "Алиас upstart успешно добавлен."
    source ~/.bashrc
else
    log "Алиас upstart уже существует в ~/.bashrc."
fi

# Завершение работы виртуального окружения
log "Завершение работы виртуального окружения."
deactivate || log "Команда deactivate не найдена. Пропускаю деактивацию виртуального окружения."

cd "$SCRIPT_DIR"

log "Скрипт завершил работу. Лог записан в $LOG_FILE."
