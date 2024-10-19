from src.blockchain import Block

def test_block_creation():
    # Создаём блок, используя 3 аргумента (index, data, previous_hash)
    block = Block(0, "Test data", "0")
    
    # Проверяем, что все атрибуты блока инициализируются правильно
    assert block.index == 0
    assert block.data == "Test data"
    assert block.previous_hash == "0"
    assert block.timestamp is not None  # Временная метка должна быть автоматически установлена
    assert block.hash is not None  # Хеш должен быть рассчитан
