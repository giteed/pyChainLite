#!/bin/bash

echo "Активация виртуального окружения..."
source venv/bin/activate || { echo "Ошибка активации виртуального окружения."; exit 1; }

# Запуск меню
python3 menu.py

# Завершение работы виртуального окружения
deactivate
