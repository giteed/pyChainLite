# modules/block_viewer.py
# Модуль для просмотра блоков
import json
from rich.console import Console

console = Console()

def view_blocks(current_blockchain):
    if current_blockchain:
        console.print(json.dumps(current_blockchain, indent=4))
    else:
        console.print("[red]Сначала загрузите блокчейн.[/red]")
