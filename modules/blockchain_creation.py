# modules/block_creation.py
# Модуль для создания блоков и просмотра блоков в текущем блокчейне

import os
import json
from rich.console import Console
from src.blockchain import Block
from datetime import datetime

console = Console()

BLOCKCHAIN_DIR = "blockchains"

def create_new_block(current_blockchain, data, user_id=None):
    """
    Создание нового блока в загруженном блокчейне.
    """
    last_block = current_blockchain["blocks"][-1]
    new_block = Block(
        index=last_block["index"] + 1,
        data={
            "data": data,
            "added_by": user_id,  # Пометка, кто добавил блок
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Время добавления блока
        },
        previous_hash=last_block["hash"]
    )

    current_blockchain["blocks"].append(new_block.__dict__)

    blockchain_file = current_blockchain["file"]
    blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)
    
    # Сохраняем новый блок в файл блокчейна
    with open(blockchain_path, 'w') as f:
        json.dump(current_blockchain, f, indent=4)
    
    console.print(f"[green]Новый блок успешно добавлен в блокчейн {current_blockchain['blocks'][0]['data']['blockchain_name']}.[/green]")
    
    return new_block  # Возвращаем созданный блок для дальнейшего использования
