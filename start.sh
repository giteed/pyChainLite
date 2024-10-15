#!/bin/bash

# URL репозитория, замените, если нужно
REPO_URL="https://github.com/giteed/pyChainLite.git"

# Проверка версии Python
if ! command -v python3 &> /dev/null; then
    echo "Python3 не установлен. Установите Python версии 3.12.x."
    exit
fi

PYTHON_VERSION=$(python3 -V 2>&1 | grep -Po '(?<=Python )([0-9]+)\.([0-9]+)')
echo "Текущая версия Python: $PYTHON_VERSION"

# Проверка наличия Git
if ! command -v git &> /dev/null; then
    echo "Git не установлен. Установите Git для продолжения."
    exit
fi

echo "Git установлен."

# Клонирование репозитория
if [ ! -d ".git" ]; then
    echo "Клонирование репозитория..."
    git clone $REPO_URL
else
    echo "Репозиторий уже инициализирован."
fi

# Создание виртуального окружения
if [ ! -d "venv" ]; then
    echo "Создание виртуального окружения..."
    python3 -m venv venv
fi

# Активация виртуального окружения
echo "Активация виртуального окружения..."
source venv/bin/activate

# Установка зависимостей
echo "Установка зависимостей..."
pip install --upgrade pip
pip install -r requirements.txt || echo "Файл requirements.txt не найден, создаю файл с базовыми зависимостями..."

# Запись базовых зависимостей в requirements.txt
cat > requirements.txt <<EOL
rich
click
flask
requests
pytest
cryptography
pyyaml
EOL

pip install -r requirements.txt

# Создание структуры проекта
echo "Создание структуры проекта..."
mkdir -p src logs tests
touch logs/.gitkeep tests/.gitkeep src/.gitkeep

# Добавление .gitignore для виртуального окружения и логов
cat > .gitignore <<EOL
venv/
logs/
__pycache__/
*.pyc
EOL

# Простое меню-интерфейс
echo "Меню pyChainLite"
echo "1. Запустить блокчейн"
echo "2. Авторизация пользователя"
echo "3. Просмотреть логи"
echo "Выберите действие (1-3): "
read action

case $action in
    1)
        echo "Запуск блокчейна..."
        # Заглушка для дальнейшей разработки
        ;;
    2)
        echo "Авторизация пользователя..."
        # Заглушка для авторизации
        ;;
    3)
        echo "Просмотр логов..."
        # Заглушка для логов
        ;;
    *)
        echo "Неверный выбор!"
        ;;
esac

# Выход из виртуального окружения
deactivate
