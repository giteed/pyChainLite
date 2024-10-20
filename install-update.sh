#!/bin/bash

# Получаем путь к директории скрипта
SCRIPT_DIR=$(dirname "$(realpath "$0")")

# Определяем пути для папок проекта и логов
PROJECT_DIR="$SCRIPT_DIR/pyChainLite"
LOG_DIR="$PROJECT_DIR/logs"
LOG_FILE="$LOG_DIR/install-update.log"
BLOCKCHAIN_DIR="$PROJECT_DIR/blockchains"
PARENT_DIR=$(dirname "$SCRIPT_DIR")

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

# Проверка наличия Python
if ! command -v python3 &> /dev/null; then
    log "Python3 не установлен. Установите Python версии 3.12.x."
    exit 1
fi

log "Python установлен: $(python3 --version)"

# Проверка наличия Git
if ! command -v git &> /dev/null; then
    log "Git не установлен. Установите Git для продолжения."
    exit 1
fi

log "Git установлен: $(git --version)"

# Перемещение папки с блокчейнами в родительскую директорию перед обновлением
if [ -d "$BLOCKCHAIN_DIR" ]; then
    log "Перемещаю папку с блокчейнами в родительскую директорию..."
    mv "$BLOCKCHAIN_DIR" "$PARENT_DIR" || { log "Ошибка перемещения блокчейнов."; exit 1; }
    log "Папка с блокчейнами перемещена в $PARENT_DIR."
else
    log "Папка с блокчейнами не найдена."
fi

# Если проекта нет или часть файлов отсутствует, клонируем репозиторий заново
if [ ! -d "$PROJECT_DIR/.git" ] || [ ! -f "$PROJECT_DIR/create_dirs.sh" ]; then
    log "Часть файлов проекта отсутствует или проект не является git-репозиторием. Клонирую заново..."
    
    # Удаляем проект, если он неполный, и клонируем заново
    rm -rf "$PROJECT_DIR"
    git clone https://github.com/giteed/pyChainLite.git "$PROJECT_DIR" || { log "Ошибка клонирования репозитория."; exit 1; }
    
    log "Клонирование завершено успешно."
fi

# Перемещаемся в папку проекта
cd "$PROJECT_DIR" || { log "Ошибка: не удается зайти в директорию проекта."; exit 1; }

# Запуск скрипта для создания папок src и tests
if [ ! -f "$PROJECT_DIR/create_dirs.sh" ]; then
    log "Ошибка: скрипт create_dirs.sh не найден даже после клонирования."
    exit 1
fi

log "Проверка и создание необходимых директорий..."
chmod +x "$PROJECT_DIR/create_dirs.sh"
chmod +x "$PROJECT_DIR/update-and-start.sh"
"$PROJECT_DIR/create_dirs.sh"

# Если проект уже существует, выполняем обновление
if [ -d "$PROJECT_DIR/.git" ]; then
    log "Проект уже существует, выполняется обновление..."
    cd "$PROJECT_DIR" || { log "Ошибка: не удается зайти в директорию проекта."; exit 1; }

    # Принудительно сбрасываем изменения и обновляем проект
    log "Сброс локальных изменений..."
    git reset --hard HEAD || { log "Ошибка при сбросе изменений."; exit 1; }
    
    log "Обновление репозитория..."
    git pull origin main || { log "Ошибка при обновлении репозитория."; exit 1; }

    log "Установка прав на выполнение для start.sh и update-and-start.sh..."
    chmod +x "$PROJECT_DIR/start.sh" || { log "Ошибка при установке прав на выполнение для start.sh."; exit 1; }
    chmod +x "$PROJECT_DIR/update-and-start.sh" || { log "Ошибка при установке прав на выполнение для update-and-start.sh."; exit 1; }
fi

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

# Предлагаем переместить папку с блокчейнами обратно
if [ -d "$PARENT_DIR/blockchains" ]; then
    echo "Желаете переместить папку с блокчейнами обратно в проект? (Y/n)"
    read -r move_back_choice
    if [ "$move_back_choice" != "n" ]; then
        log "Перемещаю папку с блокчейнами обратно в проект..."
        mv "$PARENT_DIR/blockchains" "$PROJECT_DIR" || { log "Ошибка перемещения блокчейнов обратно."; exit 1; }
        log "Папка с блокчейнами успешно перемещена обратно в проект."
    else
        log "Пользователь выбрал не перемещать блокчейны обратно."
        echo "🟢 [green]Папка с блокчейнами осталась в $PARENT_DIR. Переместите её вручную при необходимости.[/green]"
    fi
fi

# Завершение работы виртуального окружения, если оно было активировано
if [[ "$VIRTUAL_ENV" != "" ]]; then
    deactivate
else
    log "Виртуальное окружение не было активировано, команда deactivate пропущена."
fi

cd "$SCRIPT_DIR"

log "Скрипт завершил работу. Лог записан в $LOG_FILE."

