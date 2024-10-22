# install-update.ps1
# Скрипт для установки и настройки pyChainLite на Windows

# Проверка наличия Python
function Check-Python {
    $python = Get-Command python3 -ErrorAction SilentlyContinue
    if (!$python) {
        Write-Host "⚠ Python 3.12 не установлен."
        $choice = Read-Host "Хотите установить Python 3.12 сейчас? (y/n)"
        if ($choice -eq "y") {
            Start-Process "https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe" -Wait
            Write-Host "⚠ Завершите установку Python вручную, а затем перезапустите этот скрипт."
            exit
        } else {
            Write-Host "⚠ Установите Python вручную, перейдя на https://www.python.org/downloads/, и перезапустите этот скрипт."
            exit
        }
    } else {
        $version = python3 --version
        Write-Host "✔ Найден $version"
    }
}

# Проверка наличия Git
function Check-Git {
    $git = Get-Command git -ErrorAction SilentlyContinue
    if (!$git) {
        Write-Host "⚠ Git не установлен."
        $choice = Read-Host "Хотите установить Git сейчас? (y/n)"
        if ($choice -eq "y") {
            Start-Process "https://github.com/git-for-windows/git/releases/download/v2.42.0.windows.1/Git-2.42.0-64-bit.exe" -Wait
            Write-Host "⚠ Завершите установку Git вручную, а затем перезапустите этот скрипт."
            exit
        } else {
            Write-Host "⚠ Установите Git вручную, перейдя на https://git-scm.com/, и перезапустите этот скрипт."
            exit
        }
    } else {
        $gitVersion = git --version
        Write-Host "✔ Найден $gitVersion"
    }
}

# Проверка виртуального окружения
function Check-Venv {
    if (!(Test-Path -Path "./venv")) {
        Write-Host "⚠ Виртуальное окружение не найдено."
        Write-Host "✔ Создаем виртуальное окружение..."
        python3 -m venv venv
    } else {
        Write-Host "✔ Виртуальное окружение уже существует."
    }
}

# Активируем виртуальное окружение
function Activate-Venv {
    Write-Host "✔ Активация виртуального окружения..."
    .\venv\Scripts\Activate
}

# Проверка и установка зависимостей
function Install-Requirements {
    Write-Host "✔ Устанавливаем зависимости..."
    pip install --upgrade pip
    pip install -r requirements.txt
}

# Клонирование проекта или обновление
function Clone-Or-Update {
    if (Test-Path -Path "./pyChainLite") {
        Write-Host "✔ Обновляем существующий проект..."
        cd pyChainLite
        git pull origin main
    } else {
        Write-Host "✔ Клонируем проект pyChainLite..."
        git clone https://github.com/giteed/pyChainLite.git
        cd pyChainLite
    }
}

# Основная функция установки
function Install-Project {
    # Проверки Python и Git
    Check-Python
    Check-Git

    # Клонирование/обновление проекта
    Clone-Or-Update

    # Проверка виртуального окружения и установка зависимостей
    Check-Venv
    Activate-Venv
    Install-Requirements

    # Установка завершена
    Write-Host "`n✔ Установка завершена!"
    Write-Host "Вы можете запустить проект с помощью:"
    Write-Host "`n    .\venv\Scripts\Activate"
    Write-Host "    python3 menu.py"
}

# Запуск установки
Install-Project
