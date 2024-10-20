# modules/blockchain_creation.py
# Модуль для создания блокчейна
import os
import json
import hashlib
from src.blockchain import Block
from rich.console import Console

console = Console()
BLOCKCHAIN_DIR = "blockchains"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_blockchain():
    blockchain_name = input("Введите имя для нового блокчейна: ").strip()
    blockchain_owner = input("Введите имя владельца блокчейна: ").strip()
    owner_password = input("Введите пароль для владельца блокчейна: ").strip()

    hashed_password = hash_password(owner_password)
    blockchain_hash = hashlib.sha256(blockchain_name.encode()).hexdigest()
    blockchain_file = f"{blockchain_hash}.json"
    blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)

    if os.path.exists(blockchain_path):
        console.print(f"[red]Блокчейн с именем '{blockchain_name}' уже существует.[/red]")
        return

    os.makedirs(BLOCKCHAIN_DIR, exist_ok=True)
    genesis_block = Block(0, {"blockchain_name": blockchain_name, "owner": blockchain_owner, "owner_password_hash": hashed_password}, "0" * 64)
    blockchain_data = {"blocks": [genesis_block.__dict__]}

    with open(blockchain_path, 'w') as f:
        json.dump(blockchain_data, f, indent=4)

    console.print(f"\nБлокчейн '{blockchain_name}' успешно создан.")
