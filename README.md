
# pyChainLite 🚀

**pyChainLite** — это простой, гибкий и модульный блокчейн, разработанный на Python для небольших децентрализованных систем. Основная цель проекта — создать лёгкий и надёжный блокчейн, который можно использовать для безопасного хранения данных в любом формате с гарантией неизменяемости. Проект прост в использовании и легко расширяется новыми функциями.

## 📋 Оглавление

- [✨ Основные особенности](#-основные-особенности)
- [🎯 Цели проекта](#-цели-проекта)
- [🛠 Запланированные функции](#-запланированные-функции)
- [💻 Системные требования](#-системные-требования)
- [📦 Установка](#-установка)
  - [🐧 Linux и 🐋 macOS](#-linux-и--macos)
  - [🪟 Windows](#-windows)
- [📃 Лицензия](#-лицензия)

## ✨ Основные особенности

| Особенность      | Описание                                                                                                                                   |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Простота**     | Каждый модуль выполняет чётко определённую задачу, без излишней сложности. Добавление данных в блок — это простое и предсказуемое действие. |
| **Надёжность**   | Данные, помещённые в блок, гарантированно остаются неизменными, что делает pyChainLite идеальным решением для хранения любых данных.        |
| **Модульность**  | Проект легко расширяется, а новые функции можно добавлять без изменения базовой структуры.                                                  |
| **Безопасность** | Используется алгоритм консенсуса PBFT (Practical Byzantine Fault Tolerance) для надёжной работы в сети с фиксированным количеством узлов.   |
| **Форматы данных** | pyChainLite позволяет сохранять данные любого типа, от текста до изображений и других медиафайлов.                                         |

## 🎯 Цели проекта

1. Разработать минималистичный и удобный блокчейн с акцентом на лёгкость использования и модульность.
2. Реализовать алгоритм консенсуса PBFT для устойчивости к сбоям в сети.
3. Обеспечить неизменяемость данных и удобную систему авторизации пользователей.
4. Реализовать поддержку гибких шаблонов для хранения данных разных форматов.

## 🛠 Запланированные функции

| Функция                                  | Описание                                                                                      |
|------------------------------------------|-----------------------------------------------------------------------------------------------|
| **Регистрация и авторизация**            | Хеширование паролей пользователей и проверка прав на добавление данных в блокчейн.             |
| **Гибкая структура блоков**              | Поддержка данных любого формата, включая текст, изображения и другие медиафайлы.              |
| **Логирование**                          | Отслеживание всех изменений в блокчейне для удобного аудита действий.                          |
| **Синхронизация узлов**                  | Поддержка синхронизации между узлами в распределенной сети.                                    |
| **Интерфейсы командной строки и веб**    | Удобный интерфейс для взаимодействия с блокчейном как через командную строку, так и через веб. |
| **Интеграция с IPFS**                    | Хранение больших данных вне блокчейна с использованием IPFS.                                   |

## 💻 Системные требования

Для корректной работы pyChainLite требуются следующие компоненты:

| Компонент          | Требование                         |
|--------------------|------------------------------------|
| **Python**         | 3.12.x или выше                    |
| **Git**            | Для управления репозиториями       |
| **Виртуальное окружение** | Поддержка Python `venv` |
| **Необходимые библиотеки** | Устанавливаются автоматически через `requirements.txt`:

| Библиотека    | Назначение                                                                 |
|---------------|---------------------------------------------------------------------------|
| `rich`        | Красивое форматирование в командной строке.                              |
| `click`       | Удобные интерфейсы командной строки.                                     |
| `flask`       | Веб-интерфейс.                                                           |
| `requests`    | Работа с HTTP-запросами.                                                 |
| `pytest`      | Для тестирования кода.                                                   |
| `cryptography`| Работа с хешированием и безопасностью данных.                            |
| `pyyaml`      | Работа с конфигурационными файлами.                                       |

## 📦 Установка

### 🐧 Linux и 🐋 macOS

1. Создайте директорию, в которую будет установлен проект:
   ```bash
   mkdir pyChainLite && cd pyChainLite
   ```

2. Скачайте и запустите установочный скрипт `start.sh`:
   ```bash
   wget https://github.com/giteed/pyChainLite/raw/main/start.sh
   chmod +x start.sh
   ./start.sh
   ```

   > **Примечание:** Скрипт `start.sh` автоматически клонирует репозиторий, устанавливает все зависимости и создаёт необходимые структуры файлов.

### 🪟 Windows

1. Создайте директорию, в которую будет установлен проект:
   ```bash
   mkdir pyChainLite && cd pyChainLite
   ```

2. Скачайте и запустите скрипт `start.bat` (будет добавлен в будущем):
   ```cmd
   curl -O https://github.com/giteed/pyChainLite/raw/main/start.bat
   start.bat
   ```

   > **Примечание:** Скрипт `start.bat` будет автоматически клонировать репозиторий и установить все необходимые зависимости. Этот файл будет добавлен в будущих версиях проекта.

## 📃 Лицензия

Этот проект распространяется под лицензией MIT. Более подробная информация доступна в файле `LICENSE`.
