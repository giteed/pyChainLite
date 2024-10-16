# src/blockchain.py
import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, user_signature):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.user_signature = user_signature
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_content = f"{self.index}{self.timestamp}{self.previous_hash}{self.data}{self.user_signature}"
        return hashlib.sha256(block_content.encode()).hexdigest()

    def __repr__(self):
        return f"Block(index={self.index}, hash={self.hash})"
