"""
Author: Alejandro Sanchez Uribe
Date: 13 Dec 19
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


def llist_to_set(llist):
    result = set()

    node = llist.head

    while node:
        result.add(node.value)
        node = node.next

    return result


def union(llist_1, llist_2):
    lst1 = list(llist_to_set(llist_1))
    lst2 = list(llist_to_set(llist_2))
    lst1.extend(lst2)

    union_lst = list(set(lst1))
    union_llist = LinkedList()

    for element in union_lst:
        union_llist.append(element)

    return union_llist


def intersection(llist_1, llist_2):
    lst1 = list(llist_to_set(llist_1))
    lst2 = list(llist_to_set(llist_2))

    intersect_lst = [element for element in lst1 if element in lst2]

    intersect_llist = LinkedList()

    for element in intersect_lst:
        intersect_llist.append(element)

    return intersect_llist


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
# prints 1, 2, 3, 4, 6, 9, 11, 21, 32, 35, 65
print(intersection(linked_list_1, linked_list_2))
# prints 4, 6, 21

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
# prints 1, 2, 3, 4, 6, 7, 8, 9, 11, 21, 23, 35, 65
print(intersection(linked_list_3, linked_list_4))
# prints an empty list


# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [None, 2]
element_2 = [None, None, None, None, None, 1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))
# prints 1, 2, None
print(intersection(linked_list_5, linked_list_6))
# prints None

# Test case 4
print(union(linked_list_1, linked_list_5))
# prints 2, 3, 4, 6, 21, 35, 65, None
print(intersection(linked_list_1, linked_list_5))
# prints 2

# Test case 5

linked_list_7 = LinkedList()

element_1 = []

for i in element_1:
    linked_list_7.append(i)

print(union(linked_list_6, linked_list_7))
# prints 1, None
print(intersection(linked_list_6, linked_list_7))
# prints an empty list
