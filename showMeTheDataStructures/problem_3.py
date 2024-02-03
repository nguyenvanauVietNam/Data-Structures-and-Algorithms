"""
problem_3.py

A. Huffman Encoding
Assume that we have a string message AAAAAAABBBCCCCCCCDDEEEEEE comprising of 25 characters to be encoded. The string message can be an unsorted one as well. We will have two phases in encoding - building the Huffman tree (a binary tree), and generating the encoded data. The following steps illustrate the Huffman encoding:

Phase I - Build the Huffman Tree
A Huffman tree is built in a bottom-up approach.

First, determine the frequency of each character in the message. In our example, the following table presents the frequency of each character.

"""

import sys
import collections

class Node(object):
    def __init__(self, char=None, priority=None):
        self.char = char
        self.priority = priority
        self.left = None
        self.right = None

    @staticmethod
    def combine_nodes(node_1, node_2):
        combine_node = Node()

        if node_1.priority <= node_2.priority:
            combine_node.left = node_1
            combine_node.right = node_2
        else:
            combine_node.left = node_2
            combine_node.right = node_1

        combine_node.priority = node_1.priority + node_2.priority

        return combine_node

    def __repr__(self):
        return "Node of character: {} | frequency: {}".format(self.char, self.priority)

class Queue(object):
    def __init__(self, string):
        counter = collections.Counter(string)
        self.arr = [Node(char=letter, priority=_[letter]) for letter in counter]
        self.sort()

    def sort(self):
        self.arr = sorted(self.arr, key=lambda x: x.priority, reverse=True)

    def combine_step(self):
        low_node_1 = self.arr.pop()
        low_node_2 = self.arr.pop()

        self.arr.append(Node.combine_nodes(node_1=low_node_1, node_2=low_node_2))
        self.sort()

class Tree(object):
    def __init__(self, queue: Queue):
        while len(queue.arr) > 1:
            queue.combine_step()

        self.root = queue.arr[0]

    def convert_to_binary(self):
        self.root = self._check_binary_code(self.root)

    @staticmethod
    def _check_binary_code(node: Node):
        if (node.left is None) and (node.right is None):
            return node

        if node.left is not None:
            node.left.freq = 1
            node.left = Tree._check_binary_code(node.left)

        if node.right is not None:
            node.right.freq = 0
            node.right = Tree._check_binary_code(node.right)

        return node

class HuffmanEncoder(object):
    def __init(self, tree: Tree):
        self.table = self._create_encoding_table(base_code='', node=tree.root)
        self.encode_dict = None
        self.decode_dict = None
        self._create_encoder()
        self._create_decoder()

    def _create_encoder(self):
        encoder_dict = {element[0]: element[1] for element in self.table}
        self.encode_dict = encoder_dict

    def _create_decoder(self):
        decoder_dict = {element[1]: element[0] for element in self.table}
        self.decode_dict = decoder_dict

    def encode(self, text: str):
        coded_text = ''.join([self.encode_dict[char] for char in text])
        return coded_text

    def decode(self, encoded_text: str):
        decoded_text = ''
        while encoded_text:
            i_decoder = 1
            while True:
                if encoded_text[:i_decoder] in self.decode_dict:
                    decoded_text += self.decode_dict[encoded_text[:i_decoder]]
                    encoded_text = encoded_text[i_decoder:]
                    break
                i_decoder += 1
        return decoded_text

    @staticmethod
    def _create_encoding_table(base_code: str, node: Node):
        if (node.left is None) and (node.right is None):
            return [(node.char, base_code + str(node.freq))]
        if node.freq == -1:
            current_code = ''
        else:
            current_code = base_code + str(node.freq)
        coding_dict = []
        if node.char is not None:
            coding_dict.append((node.char, current_code + str(node.freq))
        if node.left is not None:
            coding_dict.extend(HuffmanEncoder._create_encoding_table(current_code, node.left))
        if node.right is not None:
            coding_dict.extend(HuffmanEncoder._create_encoding_table(current_code, node.right))
        return coding_dict

def huffman_encoding(data: str):
    if len(data) == 0:
        print("Introduce a non-null string")
        return
    temp_queue = Queue(string=data)
    temp_tree = Tree(queue=temp_queue)
    temp_tree.convert_to_binary()
    temp_encoder = HuffmanEncoder(temp_tree)
    return temp_encoder.encode(data), temp_encoder

def huffman_decoding(data: str, encoder: HuffmanEncoder):
    return encoder.decode(data)

if __name__ == "__main__":
    print('Test Case 1:')
    empty_sentence = ""
    print("The size of the data is: {}\n".format(sys.getsizeof(empty_sentence)))
    print("The content of the data is: {}\n".format(empty_sentence))
    encoded_data, tree = huffman_encoding(empty_sentence)
    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    print('Test Case 2:')
    no_data = None
    print("The size of the data is: {}\n".format(sys.getsizeof(no_data)))
    encoded_data = huffman_encoding(no_data)
    if encoded_data is not None:
        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print("The content of the encoded data is: {}\n".format(encoded_data))
        decoded_data = huffman_decoding(encoded_data, tree)
        print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print("The content of the encoded data is: {}\n".format(decoded_data))
    else:
        print("No encoded data to decode.")

    print('Test Case 3:')
    long_sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    print("The size of the data is: {}\n".format(sys.getsizeof(long_sentence)))
    print("The content of the data is: {}\n".format(long_sentence))
    encoded_data, tree = huffman_encoding(long_sentence)
    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
    