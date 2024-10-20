# Основное меню с разделением на блоки
def display_menu():
    table = Table(title="Меню pyChainLite", show_header=True, header_style="bold cyan")
    
    # Блок 1: Операции с блокчейнами
    table.add_column("Номер", style="dim")
    table.add_column("Действие", style="bold")
    
    table.add_row("1", "🧱 Создать новый блокчейн")
    table.add_row("2", "📂 Загрузить блокчейн")
    table.add_row("5", "📜 Список блокчейнов")
    
    # Пустая строка для визуального разделения блоков
    table.add_row("", "")
    
    # Блок 2: Операции с блоками
    table.add_row("3", "📝 Создать новый блок")
    table.add_row("4", "🔍 Просмотреть блоки")
    
    # Пустая строка для визуального разделения блоков
    table.add_row("", "")
    
    # Блок 3: Тестирование
    table.add_row("6", "🧪 Запустить тесты")
    
    # Пустая строка для визуального разделения блоков
    table.add_row("", "")
    
    # Блок 4: Обновление проекта
    table.add_row("7", "🔄 Обновить проект")
    
    # Пустая строка для разделения выхода
    table.add_row("", "")
    
    # Выход
    table.add_row("q/Q", "🚪 Выйти")

    console.print(table)

# Основной цикл программы
def main():
    while True:
        display_menu()
        choice = input("Выберите действие (1-7 или q/Q): ").strip().lower()
        
        if choice == '1':
            create_blockchain()
        elif choice == '2':
            load_blockchain()
        elif choice == '3':
            create_new_block()
        elif choice == '4':
            if current_blockchain:
                console.print(json.dumps(current_blockchain, indent=4))
            else:
                console.print("[bold red]Сначала загрузите блокчейн.[/bold red]")
        elif choice == '5':
            list_blockchains()
        elif choice == '6':
            run_tests()
        elif choice == '7':
            update_project()
        elif choice == 'q':
            console.print("[bold green]Выход...[/bold green]")
            break
        else:
            console.print("[bold red]Неверный выбор. Пожалуйста, выберите действие от 1 до 7 или q для выхода.[/bold red]")

if __name__ == "__main__":
    main()
