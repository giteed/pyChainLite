#!/bin/bash

# Определяем URL репозитория и название папки проекта
REPO_URL="https://github.com/giteed/pyChainLite.git"
PROJECT_DIR="pyChainLite"
LOG_DIR="$PROJECT_DIR/logs"
LOG_FILE="$LOG_DIR/install-update.log"

# Проверяем наличие Python
if ! command -v python3 &> /dev/null; then
    echo "Python3 не установлен. Установите Python версии 3.12.x." | tee -a "$LOG_FILE"
    exit
fi

# Проверяем наличие Git
if ! command -v git &> /dev/null; then
    echo "Git не установлен. Установите Git для продолжения." | tee -a "$LOG_FILE"
    exit
fi

# Создаем папку проекта и клонируем репозиторий, если она не существует
if [ ! -d "$PROJECT_DIR" ]; then
    echo "Клонирование репозитория $REPO_URL в папку $PROJECT_DIR..." | tee -a "$LOG_FILE"
    git clone "$REPO_URL" "$PROJECT_DIR" || { echo "Ошибка клонирования репозитория." | tee -a "$LOG_FILE"; exit 1; }
    
    # Делаем start.sh исполняемым
    chmod +x "$PROJECT_DIR/start.sh" || { echo "Ошибка при установке прав на выполнение для start.sh." | tee -a "$LOG_FILE"; exit 1; }
else
    echo "Проект уже существует, выполняется обновление..." | tee -a "$LOG_FILE"
    cd "$PROJECT_DIR" || { echo "Ошибка: не удается зайти в директорию проекта." | tee -a "$LOG_FILE"; exit 1; }

    # Принудительно сбрасываем изменения и обновляем проект
    git reset --hard HEAD || { echo "Ошибка при сбросе изменений." | tee -a "$LOG_FILE"; exit 1; }
    git pull origin main || { echo "Ошибка при обновлении репозитория." | tee -a "$LOG_FILE"; exit 1; }

    # Восстанавливаем start.sh, если он был удален
    if [ ! -f "start.sh" ];then
        echo "Файл start.sh был удалён локально, восстанавливаю его из репозитория..." | tee -a "$LOG_FILE"
        git checkout origin/main -- start.sh || { echo "Ошибка при восстановлении start.sh." | tee -a "$LOG_FILE"; exit 1; }
    fi

    # Устанавливаем права на выполнение для start.sh
    chmod +x "start.sh" || { echo "Ошибка при установке прав на выполнение для start.sh после обновления." | tee -a "$LOG_FILE"; exit 1; }
    cd ..
fi

# Создаем папку для логов, если она не существует
if [ ! -d "$LOG_DIR" ]; then
    mkdir -p "$LOG_DIR" || { echo "Ошибка создания директории для логов." | exit 1; }
fi

# Перемещаемся в директорию проекта для установки зависимостей
cd "$PROJECT_DIR" || { echo "Ошибка: не удается зайти в директорию проекта." | tee -a "$LOG_FILE"; exit 1; }

# Создаем виртуальное окружение, если оно не создано
if [ ! -d "venv" ]; then
    echo "Создание виртуального окружения..." | tee -a "$LOG_FILE"
    python3 -m venv venv || { echo "Ошибка создания виртуального окружения." | tee -a "$LOG_FILE"; exit 1; }
fi

# Активация виртуального окружения
echo "Активация виртуального окружения..." | tee -a "$LOG_FILE"
source venv/bin/activate || { echo "Ошибка активации виртуального окружения." | tee -a "$LOG_FILE"; exit 1; }

# Установка зависимостей
if [ -f "requirements.txt" ]; then
    echo "Установка зависимостей..." | tee -a "$LOG_FILE"
    pip install --upgrade pip || { echo "Ошибка обновления pip." | tee -a "$LOG_FILE"; exit 1; }
    pip install -r requirements.txt || { echo "Ошибка установки зависимостей." | tee -a "$LOG_FILE"; exit 1; }
else
    echo "Файл requirements.txt не найден. Установка зависимостей невозможна." | tee -a "$LOG_FILE"
    exit 1
fi

# Проверка успешности установки
echo "Установка или обновление завершены успешно." | tee -a "$LOG_FILE"
deactivate
cd ..

# Завершение работы скрипта
echo "Скрипт завершил работу. Лог записан в $LOG_FILE."
