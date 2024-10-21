# modules/blockchain_creation.py
def main():
    current_blockchain = None

    while True:
        # Меню и вывод блокчейна, который сейчас используется
        console.print(f"\n[bold]Текущий блокчейн:[/bold] [cyan]{current_blockchain['name'] if current_blockchain else 'Блокчейн не загружен'}[/cyan]")
        display_menu()

        choice = input("Введите ваш выбор: ").strip().lower()

        if choice == '1':
            # Создать новый блокчейн
            blockchain_name = input("Введите имя нового блокчейна: ").strip()
            current_blockchain = create_blockchain(blockchain_name)  # Убираем owner_name, он больше не нужен
        elif choice == '2':
            # Загрузить блокчейн
            blockchain_name = input("Введите имя блокчейна для загрузки: ").strip()
            current_blockchain = load_blockchain(blockchain_name)
        elif choice == '3':
            # Список блокчейнов
            list_blockchains()
        elif choice == '4':
            # Создать новый блок в текущем блокчейне
            if current_blockchain:
                create_new_block(current_blockchain)
            else:
                console.print("[red]Блокчейн не загружен. Сначала загрузите или создайте блокчейн.[/red]")
        elif choice == 'q':
            console.print("Выход...")
            break
        else:
            console.print("[red]Неверный выбор, попробуйте снова.[/red]")

if __name__ == "__main__":
    main()
