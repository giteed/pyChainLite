# create_dirs.sh
#!/bin/bash

# Создаем папку src, если она не существует
if [ ! -d "src" ]; then
    mkdir src
    touch src/__init__.py  # Инициализация пакета
    echo "Папка src создана."
else
    echo "Папка src уже существует."
fi

# Создаем папку tests, если она не существует
if [ ! -d "tests" ]; then
    mkdir tests
    touch tests/__init__.py  # Инициализация пакета
    echo "Папка tests создана."
else
    echo "Папка tests уже существует."
fi
