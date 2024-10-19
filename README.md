# pyChainLite 🚀

**pyChainLite** — это простой, гибкий и модульный блокчейн, разработанный на Python для небольших децентрализованных систем. Основная цель проекта — создать лёгкий и надёжный блокчейн, который можно использовать для безопасного хранения данных в любом формате с гарантией неизменяемости. Проект прост в использовании и легко расширяется новыми функциями.

## 📋 Оглавление

- [✨ Основные особенности](#-основные-особенности)
- [🎯 Цели проекта](#-цели-проекта)
- [🛠 Запланированные функции](#-запланированные-функции)
- [💻 Системные требования](#-системные-требования)
- [📦 Установка](#-установка)
  - [🐧 Linux и 🐋 macOS](#-linux-и-мacos)
  - [🪟 Windows через PowerShell](#windows-через-powershell)
- [🚀 Запуск](#запуск)
- [🧪 Тестирование](#тестирование)
- [📈 Прогресс проекта](#прогресс-проекта)
- [🛠 План разработки](#план-разработки)
- [📃 Лицензия](#-лицензия)

## ✨ Основные особенности

| Особенность      | Описание                                                                                                                                   |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Простота**     | Каждый модуль выполняет чётко определённую задачу, без излишней сложности. Добавление данных в блок — это простое и предсказуемое действие. |
| **Надёжность**   | Данные, помещённые в блок, гарантированно остаются неизменными, что делает pyChainLite идеальным решением для хранения любых данных.        |
| **Модульность**  | Проект легко расширяется, а новые функции можно добавлять без изменения базовой структуры.                                                  |
| **Безопасность** | Используется алгоритм консенсуса PBFT (Practical Byzantine Fault Tolerance) для надёжной работы в сети с фиксированным количеством узлов.   |
| **Форматы данных** | pyChainLite позволяет сохранять данные любого типа, от текста до изображений и других медиафайлов.                                         |

[🔝 Вернуться к оглавлению](#-оглавление)

## 🎯 Цели проекта

1. Разработать минималистичный и удобный блокчейн с акцентом на лёгкость использования и модульность.
2. Реализовать алгоритм консенсуса PBFT для устойчивости к сбоям в сети.
3. Обеспечить неизменяемость данных и удобную систему авторизации пользователей.
4. Реализовать поддержку гибких шаблонов для хранения данных разных форматов.

[🔝 Вернуться к оглавлению](#-оглавление)

## 🛠 Запланированные функции

| Функция                                  | Описание                                                                                      |
|------------------------------------------|-----------------------------------------------------------------------------------------------|
| **Регистрация и авторизация**            | Хеширование паролей пользователей и проверка прав на добавление данных в блокчейн.             |
| **Гибкая структура блоков**              | Поддержка данных любого формата, включая текст, изображения и другие медиафайлы.              |
| **Логирование**                          | Отслеживание всех изменений в блокчейне для удобного аудита действий.                          |
| **Синхронизация узлов**                  | Поддержка синхронизации между узлами в распределённой сети.                                    |
| **Интерфейсы командной строки и веб**    | Удобный интерфейс для взаимодействия с блокчейном как через командную строку, так и через веб. |
| **Интеграция с IPFS**                    | Хранение больших данных вне блокчейна с использованием IPFS.                                   |

[🔝 Вернуться к оглавлению](#-оглавление)

## 💻 Системные требования

Для корректной работы pyChainLite требуются следующие компоненты:

| Компонент          | Требование                         |
|--------------------|------------------------------------|
| **Python**         | 3.12.x или выше                    |
| **Git**            | Для управления репозиториями       |
| **Виртуальное окружение** | Поддержка Python `venv` |
| **Необходимые библиотеки** | Устанавливаются автоматически через `requirements.txt` |

### Библиотеки

| Библиотека    | Назначение                                                                 |
|---------------|---------------------------------------------------------------------------|
| `rich`        | Красивое форматирование в командной строке.                              |
| `click`       | Удобные интерфейсы командной строки.                                     |
| `flask`       | Веб-интерфейс.                                                           |
| `requests`    | Работа с HTTP-запросами.                                                 |
| `pytest`      | Для тестирования кода.                                                   |
| `cryptography`| Работа с хешированием и безопасностью данных.                            |
| `pyyaml`      | Работа с конфигурационными файлами.                                      |

[🔝 Вернуться к оглавлению](#-оглавление)

## 📦 Установка

### 🐧 Linux и 🐋 macOS

Для установки проекта на **Linux** или **macOS**, выполните следующую команду в терминале:

```bash
wget -O install-update.sh https://raw.githubusercontent.com/giteed/pyChainLite/main/install-update.sh && chmod +x install-update.sh && ./install-update.sh
```

[🔝 Вернуться к оглавлению](#-оглавление)

### 🪟 Windows через PowerShell

**⚠ Внимание: скрипт для Windows в процессе доработки. Использование может вызвать ошибки.**

Для установки проекта на **Windows** выполните следующую команду в PowerShell:

```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/giteed/pyChainLite/refs/heads/main/install-update.ps1" -OutFile "install-update.ps1"; ./install-update.ps1
```

[🔝 Вернуться к оглавлению](#-оглавление)

## 🚀 Запуск

После установки проекта для запуска используйте следующий скрипт:

### Для Linux/macOS:

```bash
./start.sh
```

### Для Windows:

В PowerShell:

```powershell
./start.bat
```

[🔝 Вернуться к оглавлению](#-оглавление)

## 🧪 Тестирование

Для запуска тестов выполните следующую команду:

```bash
pytest
```

Убедитесь, что у вас установлены все необходимые зависимости для тестов. Вы можете установить их с помощью:

```bash
pip install -r requirements.txt
```

[🔝 Вернуться к оглавлению](#-оглавление)

## 📈 Прогресс проекта

Чтобы узнать о том, что уже реализовано и какие шаги были выполнены, ознакомьтесь с файлом [Прогресс проекта](docs/project-progress.md).

[🔝 Вернуться к оглавлению](#-оглавление)

## 🛠 План разработки

Для подробного плана по добавлению записи блоков в файлы и поддержке больших данных см. файл [План разработки](docs/development-plan.md).

[🔝 Вернуться к оглавлению](#-оглавление)

## 📃 Лицензия

Этот проект распространяется под лицензией MIT. Более подробная информация доступна в файле `LICENSE`.

[🔝 Вернуться к оглавлению](#-оглавление)
