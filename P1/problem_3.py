"""
Author: Alejandro Sanchez Uribe
Date: 15 Dec 19
"""
import sys


class HuffmanChar:
    def __init__(self, char, freq):
        self.char = char
        self.code = ''
        self.isTrimmed = False
        self.freq = freq

    def get_char(self):
        return self.char

    def get_code(self):
        return self.code

    def set_code(self, code):
        self.code = code

    def get_freq(self):
        return self.freq

    def trim(self):
        self.isTrimmed = True
        self.freq = 0

    def __lt__(self, other):
        return self.freq < other

    def __eq__(self, other):
        return self.freq == other

    def __gt__(self, other):
        return self.freq > other

    def __repr__(self):
        if not self.isTrimmed:
            return str(self.freq) + ':' + self.char
        else:
            return self.char + '(' + self.code + ')'

    def __add__(self, other):
        return other + self.freq

    def __radd__(self, other):
        return self.freq + other


class Node:
    def __init__(self, value):
        self.isTrimmed = False
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def get_left(self):
        return self.left

    def set_left(self, left):
        self.left = left

    def has_left(self):
        return self.left is not None

    def get_right(self):
        return self.right

    def set_right(self, right):
        self.right = right

    def has_right(self):
        return self.right is not None

    def trim(self):
        if isinstance(self.value, HuffmanChar):
            self.value.trim()
        else:
            self.value = 0
            self.isTrimmed = True
            if self.left:
                self.left.trim()
            if self.right:
                self.right.trim()

    def __lt__(self, other):
        return self.value < other

    def __eq__(self, other):
        return self.value == other

    def __gt__(self, other):
        return self.value > other

    def __repr__(self):
        if not self.isTrimmed:
            return '[{x}[{y}|{z}]]'.format(x=self.value, y=self.get_left(), z=self.get_right())
        return '[{y}|{z}]'.format(y=self.get_left(), z=self.get_right())


class HuffmanTree:
    def __init__(self):
        self.root = None
        self.encode_cache = dict()

    def get_root(self):
        return self.root

    def encode_tree(self, root, prefix):
        if isinstance(root.get_value(), HuffmanChar):
            root.get_value().set_code(prefix)
            self.encode_cache[root.get_value().get_char()] = root.get_value().get_code()
            return

        if root.has_left():
            self.encode_tree(root.get_left(), prefix+'0')
        if root.has_right():
            self.encode_tree(root.get_right(), prefix + '1')

    def build_tree(self, freq_dict):
        nodes = []
        for key, value in freq_dict.items():
            nodes.append(Node(HuffmanChar(key, value)))
        nodes.sort(reverse=True)

        while len(nodes) > 1:
            current_node_1 = nodes.pop()
            current_node_2 = nodes.pop()
            next_node_value = current_node_1.get_value() + current_node_2.get_value()
            next_node = Node(next_node_value)

            if current_node_1 < current_node_2:
                next_node.set_left(current_node_1)
                next_node.set_right(current_node_2)
            else:
                next_node.set_left(current_node_2)
                next_node.set_right(current_node_1)

            nodes.append(next_node)
            nodes.sort(reverse=True)

        self.root = nodes[0]
        self.root.trim()
        self.encode_tree(self.root, '0')

    def encode(self, data_decoded):
        data_encoded = ''

        for char in data_decoded:
            data_encoded += self.encode_cache[char]

        return data_encoded

    def decode_character(self, root, data_encoded):
        data_encoded = data_encoded[1:]
        data_decoded = ''

        if isinstance(root.get_value(), HuffmanChar):
            data_decoded += root.get_value().get_char()
            return data_encoded, data_decoded
        else:
            if data_encoded[0] == '0':
                data_encoded, data_decoded = self.decode_character(root.get_left(), data_encoded)
            elif data_encoded[0] == '1':
                data_encoded, data_decoded = self.decode_character(root.get_right(), data_encoded)

        return data_encoded, data_decoded

    def decode(self, data_encoded):
        data_decoded = ''

        while len(data_encoded) > 1:
            data_encoded, char_decoded = self.decode_character(self.root, data_encoded)
            data_decoded += char_decoded

        return data_decoded


def frequency_counter(string):
    freq_dict = dict()

    for char in string:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1

    return freq_dict


def huffman_encoding(data_decoded):
    freq_dict = frequency_counter(data_decoded)
    huffman_tree = HuffmanTree()
    huffman_tree.build_tree(freq_dict)

    data_encoded = huffman_tree.encode(data_decoded)

    return data_encoded, huffman_tree


def huffman_decoding(data_encoded, huffman_tree):
    return huffman_tree.decode(data_encoded)


# test cases below:

# test case 1
print('- TEST CASE 1 -')
a_great_sentence = "The bird is the word"

print("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
print("The content of the data is: {}".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
print("The content of the encoded data is: {}".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
print("The content of the decoded data is: {}".format(decoded_data))

# test case 2 - all letters included
print('\n- TEST CASE 2 -')
a_great_sentence = 'The quick brown fox jumps over the lazy dog'

print("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
print("The content of the data is: {}".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
print("The content of the encoded data is: {}".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
print("The content of the decoded data is: {}".format(decoded_data))

# test case 3 - long paragraph
print('\n- TEST CASE 3 -')
a_great_sentence = 'In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends' \
                   ' of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or' \
                   ' to eat: it was a hobbit-hole, and that means comfort.'

print("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
print("The content of the data is: {}".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
print("The content of the encoded data is: {}".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
print("The content of the decoded data is: {}".format(decoded_data))

# test case 3 - same letter
print('\n- TEST CASE 3 -')
a_great_sentence = 'AAAAAAAAAAAA'

print("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
print("The content of the data is: {}".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
print("The content of the encoded data is: {}".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
print("The content of the decoded data is: {}".format(decoded_data))
