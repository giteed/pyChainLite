# modules/arg_parser.py
# Модуль для обработки аргументов командной строки

import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Создание блока в блокчейне")

    # Добавляем аргументы, которые можно передать через командную строку
    parser.add_argument('-d', '--data', type=str, help="Данные для блока", required=False)
    parser.add_argument('-o', '--owner', type=str, help="Владелец блокчейна", required=False)
    
    # Разбор аргументов
    args = parser.parse_args()

    # Возвращаем аргументы в виде словаря
    return vars(args)
