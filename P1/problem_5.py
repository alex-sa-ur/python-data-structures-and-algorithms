"""
Author: Alejandro Sanchez Uribe
Date: 14 Dec 19
"""

import datetime
import hashlib


class Block:
    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = (str(self.data) + str(self.timestamp) + str(self.previous_hash)).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def __repr__(self):
        output = '----------------\n'
        output += str(self.timestamp) + '\n'
        output += str(self.data) + '\n'
        output += str(self.hash) + '\n'
        output += str(self.previous_hash) + '\n'
        output += '----------------\n'

        return output


class Chain:
    def __init__(self):
        self.head = None
        self.num_elements = 0
        self.cache = dict()

    def append(self, value):
        time = datetime.datetime.now(datetime.timezone.utc)

        if self.head is None:
            new_node = Block(time, value, None)
        else:
            new_node = Block(time, value, self.head.hash)

        self.num_elements += 1
        self.cache[new_node.previous_hash] = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return

        temp = self.head
        self.head = self.cache[self.head.previous_hash]

        return temp

    def print_chain(self):
        if self.head is None:
            print('----------------\n Empty Chain\n----------------\n')

        node = self.head

        while node:
            print(node)
            node = self.cache[node.previous_hash]

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


# test cases below:

test_chain = Chain()

test_block_value_1 = 'this is the first block'
test_chain.append(test_block_value_1)

test_block_value_2 = 'this is the second block'
test_chain.append(test_block_value_2)

test_block_value_3 = 'this is the third block'
test_chain.append(test_block_value_3)

test_block_value_4 = 'this is the fourth block'
test_chain.append(test_block_value_4)

test_block_value_5 = None
test_chain.append(test_block_value_5)

test_block_value_6 = 10000
test_chain.append(test_block_value_6)

test_block_value_7 = ['test block', 7, None]
test_chain.append(test_block_value_7)

print('TEST PRINT - 1 -')
test_chain.print_chain()
# prints blocks in the reverse chronological order:
# ['test block', 7, None] , 10000 , None, 'this is the fourth block',
# 'this is the third block', 'this is the second block', 'this is the first block'

test_chain2 = Chain()
test_block2_value_1 = 'this is the first block - 2'
test_chain2.append(test_block2_value_1)

print('TEST PRINT - 2A -')
test_chain2.print_chain()
# prints block with value 'this is the first block - 2'

test_chain2.pop()

print('TEST PRINT - 2B -')
test_chain2.print_chain()
# prints empty chain

test_block2_value_2 = 'this is the second block - 2'
test_chain2.append(test_block2_value_2)

print('TEST PRINT - 3 -')
test_chain2.print_chain()
# prints block with value 'this is the second block - 2'

test_chain2.append(test_block2_value_1)

print('TEST PRINT - 4A -')
test_chain2.print_chain()
# prints blocks in the reverse chronological order:
# 'this is the first block - 2', 'this is the second block - 2'

test_chain2.pop()
print('TEST PRINT - 4B -')
test_chain2.print_chain()
# prints 'this is the first block - 2'
