from src.blockchain import Block

def test_block_creation():
    # Создаём блок, используя 4 аргумента (index, previous_hash, data, timestamp)
    block = Block(0, "0", "Test data", "2024-10-19 12:00:00")
    
    # Проверяем, что все атрибуты блока инициализируются правильно
    assert block.index == 0
    assert block.previous_hash == "0"
    assert block.data == "Test data"
    assert block.timestamp == "2024-10-19 12:00:00"
    
    # Проверяем, что хеш блока вычисляется корректно
    assert block.hash is not None
