# tests/test_blockchain.py
from src.blockchain import Block

def test_block_creation():
    """
    Тест на создание блока.
    Проверяет корректное создание блока с переданными данными и вычисление хеша.
    """
    block = Block(1, "Тестовые данные", "0" * 64)
    
    # Проверяем индекс блока
    assert block.index == 1
    
    # Проверяем данные блока
    assert block.data == "Тестовые данные"
    
    # Проверяем хеш предыдущего блока
    assert block.previous_hash == "0" * 64
    
    # Проверяем, что хеш блока был успешно сгенерирован
    assert len(block.hash) == 64  # Длина SHA-256 хеша должна быть 64 символа

def test_block_hash_is_unique():
    """
    Тест на уникальность хеша.
    Проверяет, что при изменении данных блока, его хеш также изменяется.
    """
    block1 = Block(1, "Данные блока 1", "0" * 64)
    block2 = Block(1, "Данные блока 2", "0" * 64)
    
    # Хеши должны отличаться, так как данные блоков разные
    assert block1.hash != block2.hash

def test_block_timestamp():
    """
    Тест на временную метку блока.
    Проверяет, что временная метка присутствует и является числом.
    """
    block = Block(1, "Тестовые данные", "0" * 64)
    
    # Проверяем, что временная метка является числом
    assert isinstance(block.timestamp, float)
