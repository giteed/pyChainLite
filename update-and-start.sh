#!/bin/bash

# Переходим в родительскую директорию
cd ..

# Запускаем обновление
./install-update.sh

# Возвращаемся в папку проекта
cd pyChainLite/

# Запускаем скрипт start.sh
./start.sh
