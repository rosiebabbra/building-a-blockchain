import hashlib

class Block:
    def __init__(self, previous_hash, transaction):
        self.transactions = transaction
        self.previous_hash = previous_hash
        arr_to_hash = "".join(transaction) + previous_hash
        self.block_hash = hashlib.sha256(arr_to_hash.encode()).hexdigest()