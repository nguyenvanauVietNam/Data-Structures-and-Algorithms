"""
Problem 5: Blockchain
A Blockchain is a sequential chain of records, similar to a linked list.
Each block contains some information and how it is connected related to the other blocks in the chain.
Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data.
For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.

We can break the blockchain down into three main parts.
First is the information hash:
We do this for the information we want to store in the blockchain such as transaction time, data, and information like the previous chain.
The next main component is the block on the blockchain:
Above is an example of attributes you could find in a Block class.

Finally you need to link all of this together in a block chain, which you will be doing by implementing it in a linked list.
All of this will help you build up to a simple but full blockchain implementation!
"""

import hashlib
import datetime
import random
import string

class Block(object):
    def __init__(self, data, previous_hash, previous_block):
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.previous_block = previous_block

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = (str(self.timestamp) +
                    str(self.data) +
                    str(self.previous_hash)).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    @property
    def get_previous_hash(self):
        return self.previous_hash

    @property
    def get_hash(self):
        return self.hash

    def __repr__(self):
        the_block = ("\nBlock Attributes:" +
                     "\n   timestamp: " + str(self.timestamp) +
                     "\n   data: " + str(self.data) +
                     "\n   previous hash: " + str(self.previous_hash) +
                     "\n   hash: " + str(self.hash))
        return the_block

class Chain(object):
    def __init(self, tail=None):
        self.tail = tail
        self.size = 0

    def get_size(self):
        return self.size

    def append(self, data):
        if data is None or data == "":
            return False

        if self.tail is None:
            self.tail = big_bang_block()
            self.size += 1
            return True

        new_block = create_new_block(data, self.tail)
        self.tail = new_block
        self.size += 1
        return True

def big_bang_block():
    return Block("1) the singularity", 0, None)

def create_new_block(data, previous_block):
    some_data = str(data)
    last_hash = 0 if previous_block is None else previous_block.hash
    return Block(some_data, last_hash, previous_block)

def main():
    chain_link = Chain()
    
    # Test Case 1: Append some blocks with random integers
    chain_link.append(big_bang_block())
    chain_link.append(random.randint(1, 9999))
    chain_link.append(random.randint(1, 9999))
    chain_link.append(random.randint(1, 9999))
    chain_link.append(random.randint(1, 9999))
    chain_link.append("")
    
    # Test Case 2: Append a block with a large random string
    data = ''.join(random.choices(string.ascii_letters, k=10000))
    chain_link.append(data)
    #Test Case 3: Add a block with data that is a very large string (a large random string)
    data = ''.join(random.choices(string.ascii_letters, k=10000))
    chain_link.append(data)
    
    print("\n-----Block Chain (link list test)-----")
    i = chain_link.get_size()
    print("\nLength of chain =", i)
    print("Going backwards through the blockchain")
    node = chain_link.tail

    while node:
        print("\nBlock #{} Attributes:".format(i))
        print("-----------------------" +
              "\n   timestamp: " + str(node.timestamp) +
              "\n   data: " + str(node.data) +
              "\n   previous hash: " + str(node.previous_hash) +
              "\n   hash: " + str(node.hash)
              )
        i -= 1
        node = node.previous_block

if __name__ == "__main__":
    main()