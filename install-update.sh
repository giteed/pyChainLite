#!/bin/bash

# Определяем абсолютный путь к текущей директории и к папкам проекта и логов
BASE_DIR=$(pwd)
PROJECT_DIR="$BASE_DIR/pyChainLite"
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

# Создаем папку для логов внутри проекта, если она не существует
if [ ! -d "$LOG_DIR" ]; then
    echo "Создание директории для логов..."
    mkdir -p "$LOG_DIR" || { echo "Ошибка создания директории для логов."; exit 1; }
fi

# Создаем файл лога, если он не существует
if [ ! -f "$LOG_FILE" ]; then
    echo "Создание файла лога..."
    touch "$LOG_FILE" || { echo "Ошибка создания файла лога."; exit 1; }
fi

# Функция для записи в лог с датой и временем
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

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

# Если проект уже существует, выполняем обновление
if [ -d "$PROJECT_DIR/.git" ]; then
    log "Проект уже существует, выполняется обновление..."
    cd "$PROJECT_DIR" || { log "Ошибка: не удается зайти в директорию проекта."; exit 1; }

    # Принудительно сбрасываем изменения и обновляем проект
    log "Сброс локальных изменений..."
    git reset --hard HEAD || { log "Ошибка при сбросе изменений."; exit 1; }
    
    log "Обновление репозитория..."
    git pull origin main || { log "Ошибка при обновлении репозитория."; exit 1; }

    log "Установка прав на выполнение для start.sh..."
    chmod +x "start.sh" || { log "Ошибка при установке прав на выполнение для start.sh."; exit 1; }
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

# Создание скрипта update-and-start.sh для обновления и запуска одной командой
log "Создание скрипта update-and-start.sh..."
cat << 'EOF' > "$BASE_DIR/update-and-start.sh"
#!/bin/bash

# Переходим в родительскую директорию
cd ..

# Запускаем обновление
./install-update.sh

# Возвращаемся в папку проекта
cd pyChainLite/

# Запускаем скрипт start.sh
./start.sh
EOF

# Делаем скрипт исполняемым
chmod +x "$BASE_DIR/update-and-start.sh" || { log "Ошибка при установке прав на выполнение для update-and-start.sh."; exit 1; }

log "Скрипт update-and-start.sh создан и готов к использованию."

# Завершение работы виртуального окружения
deactivate
cd "$BASE_DIR"

log "Скрипт завершил работу. Лог записан в $LOG_FILE."
