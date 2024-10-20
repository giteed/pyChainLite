#!/bin/bash

# Получаем путь к директории скрипта
SCRIPT_DIR=$(dirname "$(realpath "$0")")

# Определяем пути для папок проекта и логов
PROJECT_DIR="$SCRIPT_DIR"
LOG_DIR="$PROJECT_DIR/logs"
LOG_FILE="$LOG_DIR/install-update.log"

# Функция для записи в лог с датой и временем
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Создаем папку для логов, если она не существует
if [ ! -d "$LOG_DIR" ]; then
    log "Создание директории для логов..."
    mkdir -p "$LOG_DIR" || { log "Ошибка создания директории для логов."; exit 1; }
fi

# Создаем файл лога, если он не существует
if [ ! -f "$LOG_FILE" ];then
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

# Если проекта нет или часть файлов отсутствует, спрашиваем подтверждение на его клонирование
if [ ! -d "$PROJECT_DIR/.git" ] || [ ! -f "$PROJECT_DIR/create_dirs.sh" ]; then
    log "Часть файлов проекта отсутствует или проект не является git-репозиторием."
    read -p "Вы хотите клонировать проект заново и заменить текущие файлы? (y/n): " confirm
    if [ "$confirm" != "y" ]; then
        log "Операция клонирования отменена пользователем."
        exit 1
    fi

    log "Клонирую заново..."

    # Проверяем, существует ли директория проекта
    if [ -d "$PROJECT_DIR" ]; then
        log "Проект уже существует, но неполный."
        read -p "Вы хотите удалить текущую папку проекта и клонировать заново? (y/n): " confirm_delete
        if [ "$confirm_delete" != "y" ]; then
            log "Операция отменена. Рекомендуется вручную удалить текущие файлы и повторить запуск скрипта."
            exit 1
        fi
        log "Удаление текущей папки проекта..."
        rm -rf "$PROJECT_DIR" || { log "Ошибка при удалении текущей папки проекта."; exit 1; }
    fi

    git clone https://github.com/giteed/pyChainLite.git "$PROJECT_DIR" || { log "Ошибка клонирования репозитория."; exit 1; }

    log "Клонирование завершено успешно."
else
    # Если проект уже существует, просто обновляем его
    cd "$PROJECT_DIR" || { log "Ошибка: не удается зайти в директорию проекта."; exit 1; }
    log "Проект уже существует, выполняется обновление..."
    
    log "Сброс локальных изменений..."
    git reset --hard HEAD || { log "Ошибка при сбросе изменений."; exit 1; }

    log "Обновление репозитория..."
    git pull origin main || { log "Ошибка при обновлении репозитория."; exit 1; }
fi

# Запуск скрипта для создания папок src и tests
if [ -f "$PROJECT_DIR/create_dirs.sh" ]; then
    log "Проверка и создание необходимых директорий..."
    chmod +x "$PROJECT_DIR/create_dirs.sh"
    "$PROJECT_DIR/create_dirs.sh"
else
    log "Скрипт create_dirs.sh не найден."
fi

log "Установка прав на выполнение для start.sh и update-and-start.sh..."
chmod +x "$PROJECT_DIR/start.sh" || { log "Ошибка при установке прав на выполнение для start.sh."; exit 1; }
chmod +x "$PROJECT_DIR/update-and-start.sh" || { log "Ошибка при установке прав на выполнение для update-and-start.sh."; exit 1; }

# Создаем виртуальное окружение, если оно не создано
if [ ! -d "$PROJECT_DIR/venv" ]; then
    log "Создание виртуального окружения..."
    python3 -m venv venv || { log "Ошибка создания виртуального окружения."; exit 1; }
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
    pip install -r requirements.txt || { log "Ошибка установки зависимостей."; exit 1; }
else
    log "Файл requirements.txt не найден. Установка зависимостей невозможна."
    exit 1
fi

log "Установка или обновление завершены успешно."

# Добавляем алиас в ~/.bashrc для команды upstart
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
