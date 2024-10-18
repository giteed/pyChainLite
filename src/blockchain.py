# src/blockchain.py
import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index                        # Номер блока в цепочке
        self.timestamp = time.time()              # Временная метка создания блока
        self.data = data                          # Данные, хранимые в блоке
        self.previous_hash = previous_hash        # Хеш предыдущего блока
        self.hash = self.calculate_hash()         # Хеш текущего блока

    def calculate_hash(self):
        """
        Вычисляет хеш для текущего блока.
        Хеш создается на основе данных блока, индекса, временной метки и хеша предыдущего блока.
        """
        block_data = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_data.encode()).hexdigest()

    def __repr__(self):
        """
        Возвращает строковое представление блока для удобства отображения.
        """
        return (f"Block(index: {self.index}, timestamp: {self.timestamp}, "
                f"data: {self.data}, previous_hash: {self.previous_hash}, hash: {self.hash})")
