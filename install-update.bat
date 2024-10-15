@echo off
setlocal

:: Определяем директории проекта и логов
set BASE_DIR=%CD%
set PROJECT_DIR=%BASE_DIR%\pyChainLite
set LOG_DIR=%PROJECT_DIR%\logs
set LOG_FILE=%LOG_DIR%\install-update.log

:: Функция для записи в лог с датой и временем
:log
    echo [%date% %time%] %1 >> %LOG_FILE%
    goto :eof

:: Проверяем существование папки проекта
if not exist "%PROJECT_DIR%" (
    call :log "Ошибка: папка проекта %PROJECT_DIR% не существует. Выполните установку проекта сначала."
    exit /b 1
)

:: Создаем папку для логов внутри проекта, если она не существует
if not exist "%LOG_DIR%" (
    call :log "Создание директории для логов..."
    mkdir "%LOG_DIR%"
    if errorlevel 1 (
        call :log "Ошибка создания директории для логов."
        exit /b 1
    )
)

:: Создаем файл лога, если он не существует
if not exist "%LOG_FILE%" (
    call :log "Создание файла лога..."
    type nul > "%LOG_FILE%"
    if errorlevel 1 (
        call :log "Ошибка создания файла лога."
        exit /b 1
    )
)

call :log "Запуск установки/обновления"

:: Проверка наличия Python
where python >nul 2>&1
if errorlevel 1 (
    call :log "Python не установлен. Установите Python версии 3.12.x."
    exit /b 1
)
for /f "delims=" %%p in ('python --version') do set PYTHON_VERSION=%%p
call :log "Python установлен: %PYTHON_VERSION%"

:: Проверка наличия Git
where git >nul 2>&1
if errorlevel 1 (
    call :log "Git не установлен. Установите Git для продолжения."
    exit /b 1
)
for /f "delims=" %%g in ('git --version') do set GIT_VERSION=%%g
call :log "Git установлен: %GIT_VERSION%"

:: Проверка, был ли проект уже клонирован
if not exist "%PROJECT_DIR%\.git" (
    call :log "Клонирование репозитория в папку %PROJECT_DIR%..."
    git clone https://github.com/giteed/pyChainLite.git "%PROJECT_DIR%"
    if errorlevel 1 (
        call :log "Ошибка клонирования репозитория."
        exit /b 1
    )
    
    :: Делаем start.bat исполняемым (в Windows не требуется chmod)
    call :log "Клонирование завершено. Переход к следующему шагу."
) else (
    call :log "Проект уже существует, выполняется обновление..."
    cd "%PROJECT_DIR%"
    
    :: Принудительно сбрасываем изменения и обновляем проект
    git reset --hard HEAD
    if errorlevel 1 (
        call :log "Ошибка при сбросе изменений."
        exit /b 1
    )

    call :log "Обновление репозитория..."
    git pull origin main
    if errorlevel 1 (
        call :log "Ошибка при обновлении репозитория."
        exit /b 1
    )

    :: Проверка наличия start.bat и его восстановление
    if not exist "start.bat" (
        call :log "Файл start.bat был удалён локально, восстанавливаю его из репозитория..."
        git checkout origin/main -- start.bat
        if errorlevel 1 (
            call :log "Ошибка при восстановлении start.bat."
            exit /b 1
        )
    )
)

:: Проверка наличия виртуального окружения
if not exist "%PROJECT_DIR%\venv" (
    call :log "Создание виртуального окружения..."
    python -m venv "%PROJECT_DIR%\venv"
    if errorlevel 1 (
        call :log "Ошибка создания виртуального окружения."
        exit /b 1
    )
) else (
    call :log "Виртуальное окружение уже существует."
)

:: Активация виртуального окружения
call :log "Активация виртуального окружения..."
call "%PROJECT_DIR%\venv\Scripts\activate.bat"
if errorlevel 1 (
    call :log "Ошибка активации виртуального окружения."
    exit /b 1
)

:: Установка зависимостей
if exist "%PROJECT_DIR%\requirements.txt" (
    call :log "Установка зависимостей из requirements.txt..."
    pip install --upgrade pip
    if errorlevel 1 (
        call :log "Ошибка обновления pip."
        exit /b 1
    )
    pip install -r "%PROJECT_DIR%\requirements.txt"
    if errorlevel 1 (
        call :log "Ошибка установки зависимостей."
        exit /b 1
    )
) else (
    call :log "Файл requirements.txt не найден. Установка зависимостей невозможна."
    exit /b 1
)

call :log "Установка или обновление завершены успешно."

:: Деактивация виртуального окружения
deactivate

:: Завершение работы
call :log "Скрипт завершил работу. Лог записан в %LOG_FILE%."
exit /b 0
