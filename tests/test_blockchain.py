# tests/test_blockchain.py
import pytest
from src.blockchain import Block

def test_block_creation():
    block = Block(0, "0", "Test data", "user_signature")
    assert block.index == 0
    assert block.previous_hash == "0"
    assert block.data == "Test data"
    assert block.user_signature == "user_signature"
    assert len(block.hash) == 64  # Хеш SHA-256 должен быть 64 символа
