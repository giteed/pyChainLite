# Определяем директории проекта и логов
$BASE_DIR = Get-Location
$PROJECT_DIR = Join-Path $BASE_DIR "pyChainLite"
$LOG_DIR = Join-Path $PROJECT_DIR "logs"
$LOG_FILE = Join-Path $LOG_DIR "install-update.log"

# Функция для записи в лог с датой и временем
function Log {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "$timestamp $args" | Out-File -Append -FilePath $LOG_FILE
}

# Создаем папку проекта, если она не существует
if (-not (Test-Path $PROJECT_DIR)) {
    Write-Host "Создание директории проекта..."
    New-Item -ItemType Directory -Path $PROJECT_DIR | Out-Null
    if (-not (Test-Path $PROJECT_DIR)) {
        Write-Host "[Ошибка] Не удалось создать директорию проекта."
        Exit 1
    }
} else {
    Write-Host "Папка проекта уже существует."
}

# Создаем папку для логов, если она не существует
if (-not (Test-Path $LOG_DIR)) {
    Write-Host "Создание директории для логов..."
    New-Item -ItemType Directory -Path $LOG_DIR | Out-Null
    if (-not (Test-Path $LOG_DIR)) {
        Write-Host "[Ошибка] Не удалось создать директорию для логов."
        Exit 1
    }
}

# Создаем файл лога, если он не существует
if (-not (Test-Path $LOG_FILE)) {
    Write-Host "Создание файла лога..."
    New-Item -ItemType File -Path $LOG_FILE | Out-Null
}

Log "Запуск установки/обновления"

# Проверяем наличие Python
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Log "Python не установлен. Установите Python версии 3.12.x."
    Write-Host "[Ошибка] Python не установлен. Установите Python версии 3.12.x."
    Exit 1
}

$pythonVersion = & python --version
Log "Python установлен: $pythonVersion"
Write-Host "Python установлен: $pythonVersion"

# Проверяем наличие Git
$git = Get-Command git -ErrorAction SilentlyContinue
if (-not $git) {
    Log "Git не установлен. Установите Git для продолжения."
    Write-Host "[Ошибка] Git не установлен. Установите Git для продолжения."
    Exit 1
}

$gitVersion = & git --version
Log "Git установлен: $gitVersion"
Write-Host "Git установлен: $gitVersion"

# Проверка, был ли проект уже клонирован
if (Test-Path "$PROJECT_DIR/.git") {
    Log "Проект уже существует, выполняется обновление..."
    Write-Host "Проект уже существует, выполняется обновление..."
    Set-Location $PROJECT_DIR

    # Принудительно сбрасываем изменения и обновляем проект
    & git reset --hard HEAD
    if ($LASTEXITCODE -ne 0) {
        Log "Ошибка при сбросе изменений."
        Write-Host "[Ошибка] Не удалось сбросить изменения."
        Exit 1
    }

    Log "Обновление репозитория..."
    & git pull origin main
    if ($LASTEXITCODE -ne 0) {
        Log "Ошибка при обновлении репозитория."
        Write-Host "[Ошибка] Не удалось обновить репозиторий."
        Exit 1
    }
} elseif (-not (Test-Path "$PROJECT_DIR/.git")) {
    Write-Host "Папка не является репозиторием. Удаление и повторное клонирование..."
    Remove-Item -Recurse -Force $PROJECT_DIR
    Log "Клонирование репозитория в папку $PROJECT_DIR..."
    & git clone https://github.com/giteed/pyChainLite.git $PROJECT_DIR
    if ($LASTEXITCODE -ne 0) {
        Log "Ошибка клонирования репозитория."
        Write-Host "[Ошибка] Не удалось клонировать репозиторий."
        Exit 1
    }
    Log "Клонирование завершено."
    Write-Host "Клонирование завершено."
}

# Остальные шаги для активации виртуального окружения и установки зависимостей
Log "Установка или обновление завершены успешно."
Write-Host "Установка или обновление завершены успешно."
