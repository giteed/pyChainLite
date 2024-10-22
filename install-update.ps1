# install-update.ps1
# PowerShell скрипт для установки и настройки проекта pyChainLite на Windows

# Проверка наличия Python
function Check-Python {
    Write-Host "Проверка наличия Python..."
    if (!(Get-Command python -ErrorAction SilentlyContinue)) {
        Write-Host "Python не найден. Необходимо установить Python 3.12.x или выше."
        exit 1
    } else {
        $pythonVersion = & python --version
        if ($pythonVersion -lt "3.12") {
            Write-Host "Версия Python слишком старая: $pythonVersion. Установите Python 3.12.x или выше."
            exit 1
        }
        Write-Host "Python найден: $pythonVersion"
    }
}

# Проверка наличия Git
function Check-Git {
    Write-Host "Проверка наличия Git..."
    if (!(Get-Command git -ErrorAction SilentlyContinue)) {
        Write-Host "Git не установлен. Необходимо установить Git."
        exit 1
    } else {
        $gitVersion = & git --version
        Write-Host "Git найден: $gitVersion"
    }
}

# Проверка и установка виртуального окружения
function Check-Venv {
    Write-Host "Проверка виртуального окружения..."
    if (!(Test-Path -Path "./venv")) {
        Write-Host "Создание виртуального окружения..."
        python -m venv venv
    }
    Write-Host "Виртуальное окружение готово."
}

# Активация виртуального окружения
function Activate-Venv {
    Write-Host "Активация виртуального окружения..."
    .\venv\Scripts\Activate
}

# Установка зависимостей
function Install-Dependencies {
    Write-Host "Установка зависимостей..."
    python -m pip install --upgrade pip
    if (Test-Path -Path "./requirements.txt") {
        python -m pip install -r requirements.txt
    } else {
        Write-Host "Файл requirements.txt не найден. Проверьте структуру проекта."
        exit 1
    }
    Write-Host "Зависимости установлены."
}

# Клонирование или обновление проекта
function Install-Project {
    if (Test-Path -Path "./pyChainLite/.git") {
        Write-Host "Обновление проекта..."
        git pull origin main
    } else {
        Write-Host "Клонирование проекта из репозитория..."
        git clone https://github.com/giteed/pyChainLite.git pyChainLite
    }
}

# Запуск меню проекта
function Run-Project {
    Write-Host "Запуск проекта..."
    Write-Host "Активируйте виртуальное окружение и выполните:"
    Write-Host "    python pyChainLite\menu.py"
}

# Основная установка
function Main {
    Check-Python
    Check-Git
    Install-Project
    Check-Venv
    Activate-Venv
    Install-Dependencies
    Run-Project
}

# Выполнение основного процесса установки
Main
