"""
BlockChain - decentralised

its almost impossible to affect integrity


[data] -> [other data] -> [more data] -> ...

[transaction] -> [transaction] -> '[bad_transaction]' ->


[messages] <- [messages] <- ...



Block : a lot of messages
"""

import random
import hashlib
import json
from time import time



class BlockChain(object):
    def __init__(self):
        self.chain = []
        self.pending_messages = []
        self.difficulty = 3

        # create a genesis_block
        genesis_block = {
            'index': 0,
            'timestamp': time(),
            'messages': [],
            'proof': 0,
            'prev_hash': "genesis_hash",
        }
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        return self.chain[-1]

    def new_block(self):
        block = {
            'index': len(self.chain),
            'timestamp': time(),
            'messages': self.pending_messages,
            'proof': 0,
            'prev_hash': self.hash(self.last_block)
        }

        return block

    def add_block(self, block):
        if block['prev_hash'] != self.hash(self.last_block):
            return False
        if not self.is_valid_proof(block):
            return False

        self.pending_messages = []
        self.chain.append(block)

        return block

    def proof_of_work(self, block):
        comp_hash = self.hash(block)
        while not comp_hash.startswith('0' * self.difficulty):
            block['proof'] += 1
            comp_hash = self.hash(block)

        return comp_hash

    def is_valid_proof(self, block):
        """
        Check if the proof is valid
        """
        return (self.hash(block).startswith('0' * self.difficulty))

    def add_message(self, sender, contents):
        """
        Creates a message instance and returns the index
        of the block that should contain it.
        """
        msg = {
            'sender': sender,
            'contents': contents,
        }

        self.pending_messages.append(msg)

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = str(raw_hash.hexdigest())

        return hex_hash

    def mine(self):
        if not self.pending_messages:
            return False

        block = self.new_block()
        self.proof_of_work(block)
        self.add_block(block)


if __name__ == "__main__":
    bc = BlockChain()

    for i in range(100):
        bc.add_message("Adi", f"{random.randint(0,100)}")
        bc.add_message("Adi", f"{random.randint(0,100)}")
        bc.mine()

    for each in bc.chain:
        print(each['proof'])
        print(each['prev_hash'])
