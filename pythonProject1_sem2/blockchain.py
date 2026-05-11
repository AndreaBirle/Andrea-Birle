import hashlib
import time

# Clasa pentru un bloc
class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(block_string.encode()).hexdigest()


# Clasa Blockchain
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        previous_block = self.get_latest_block()
        new_block = Block(len(self.chain), data, previous_block.hash)
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # verificare hash curent
            if current.hash != current.calculate_hash():
                return False

            # verificare legatura
            if current.previous_hash != previous.hash:
                return False

        return True


# Testare
if __name__ == "__main__":
    blockchain = Blockchain()

    blockchain.add_block("Prima tranzactie")
    blockchain.add_block("A doua tranzactie")
    blockchain.add_block("A treia tranzactie")

    # Afisare blockchain
    for block in blockchain.chain:
        print("Index:", block.index)
        print("Data:", block.data)
        print("Hash:", block.hash)
        print("Prev Hash:", block.previous_hash)
        print("-" * 30)

    # Verificare validitate
    print("Blockchain valid?", blockchain.is_valid())