Блокчейн не загружен
Выберите действие (1-7, H или Q): 6
🧪 Запуск тестов...
================================================= test session starts ==================================================
platform linux -- Python 3.12.3, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/uadmin24/Загрузки/wwww/pyChainLite
collected 8 items                                                                                                      

src/test_blockchain.py ...                                                                                       [ 37%]
tests/test_block_creation.py F                                                                                   [ 50%]
tests/test_blockchain.py .                                                                                       [ 62%]
tests/test_blockchain_creation.py .                                                                              [ 75%]
tests/test_blockchain_listing.py .                                                                               [ 87%]
tests/test_blockchain_loading.py .                                                                               [100%]

======================================================= FAILURES =======================================================
________________________________________________ test_create_new_block _________________________________________________

monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7986696b6c00>, cleanup_blockchain = None

    def test_create_new_block(monkeypatch, cleanup_blockchain):
        # Создаем тестовый блокчейн
        blockchain_name = "test_block_creation"
        blockchain_file = f"{hashlib.sha256(blockchain_name.encode()).hexdigest()}.json"
        blockchain_path = os.path.join(BLOCKCHAIN_DIR, blockchain_file)
    
        blockchain_data = {
            "blocks": [{
                "index": 0,
                "data": {
                    "blockchain_name": blockchain_name,
                    "owner": "owner_name"
                },
                "previous_hash": "0" * 64,
                "hash": hashlib.sha256("test_data".encode()).hexdigest()
            }],
            "file": blockchain_file
        }
    
        # Создание папки для блокчейнов, если её нет
        os.makedirs(BLOCKCHAIN_DIR, exist_ok=True)
    
        # Сохраняем тестовый блокчейн в файл
        with open(blockchain_path, 'w') as f:
            json.dump(blockchain_data, f, indent=4)
    
        # Mock user inputs
        inputs = iter(["new block data"])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
        # Загружаем блокчейн и создаем новый блок
        new_block_data = "new block data"
>       create_new_block(blockchain_data, new_block_data)
E       NameError: name 'create_new_block' is not defined

tests/test_block_creation.py:49: NameError
=============================================== short test summary info ================================================
FAILED tests/test_block_creation.py::test_create_new_block - NameError: name 'create_new_block' is not defined
============================================= 1 failed, 7 passed in 0.07s ==============================================
Ошибка при запуске тестов: Command '['pytest']' returned non-zero exit status 1.
