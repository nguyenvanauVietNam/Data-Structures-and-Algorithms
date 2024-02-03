"""
Problem 6: Union and Intersection

Union and Intersection of Two Linked Lists
Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. For example, the union of A = [1, 2] and B = [3, 4] is [1, 2, 3, 4].

The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both sets A and B. For example, the intersection of A = [1, 2, 3] and B = [2, 3, 4] is [2, 3].

You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.

We have provided a code template below, you are not required to use it:
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size

def union(llist_1, llist_2):
    # Create sets to store unique values
    unique_values = set()
    result_list = LinkedList()

    current = llist_1.head
    while current:
        unique_values.add(current.value)
        current = current.next

    current = llist_2.head
    while current:
        unique_values.add(current.value)
        current = current.next

    for value in unique_values:
        result_list.append(value)

    return result_list

def intersection(llist_1, llist_2):
    # Create sets to store unique values
    set_1 = set()
    set_2 = set()
    result_list = LinkedList()

    current = llist_1.head
    while current:
        set_1.add(current.value)
        current = current.next

    current = llist_2.head
    while current:
        set_2.add(current.value)
        current = current.next

    common_values = set_1.intersection(set_2)

    for value in common_values:
        result_list.append(value)

    return result_list

# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("Test Case 1 - Union:", union(linked_list_1, linked_list_2))
print("Test Case 1 - Intersection:", intersection(linked_list_1, linked_list_2))

# Test case 2
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("Test Case 2 - Union:", union(linked_list_3, linked_list_4))
print("Test Case 2 - Intersection:", intersection(linked_list_3, linked_list_4))
