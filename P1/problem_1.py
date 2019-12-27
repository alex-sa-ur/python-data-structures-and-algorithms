"""
Author: Alejandro Sanchez Uribe
Date: 12 Dec 19
"""


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

    def get_key(self):
        return self.key

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def get_previous(self):
        return self.previous

    def set_previous(self, new_previous):
        self.previous = new_previous


class DoublyLinkedList:
    def __init__(self):
        self.num_elements = 0
        self.head = None
        self.tail = None

    def get_head(self):
        return self.head

    def set_head(self, new_node):
        self.head = new_node

    def get_tail(self):
        return self.tail

    def set_tail(self, new_node):
        self.tail = new_node

    def _is_empty(self):
        return self.num_elements == 0

    def get_size(self):
        return self.num_elements

    def enqueue(self, node):
        new_node = node

        if self._is_empty():
            self.head = new_node
            self.tail = self.head
        else:
            new_node.set_previous(self.tail)
            self.tail.set_next(new_node)
            self.tail = self.tail.get_next()

        self.num_elements += 1

    def dequeue(self):
        if self._is_empty():
            return None

        node = self.head
        self.head = self.head.get_next()
        self.head.set_previous(None)
        self.num_elements -= 1
        return node


class LRUCache(object):
    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = dict()
        self.queue = DoublyLinkedList()

    def get(self, key):
        # Cache Hit - Retrieve item from provided key
        # Cache Miss - Return -1 if nonexistent.

        if self.capacity == 0:
            return -1

        if key in self.cache:
            # move to back of queue
            node = self.cache[key]

            if node == self.queue.get_head():
                self.queue.dequeue()

            if node == self.queue.get_tail():
                self.queue.set_tail(self.queue.get_tail().get_previous())

            if node != self.queue.get_head() and node != self.queue.get_tail():
                if node.get_previous():
                    node.get_previous().set_next(node.get_next())
                if node.get_next():
                    node.get_next().set_previous(node.get_previous())

                node.set_previous(None)
                node.set_next(None)

            self.queue.enqueue(node)
            return self.cache[key].get_value()
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache.
        # If the cache is at capacity remove the oldest item.
        if self.capacity == 0:
            print('Capacity of 0, cannot set values')
            return

        if key in self.cache:
            # move to back of queue
            print('', end='')
        else:
            if self.queue.get_size() == self.capacity:
                self.cache.pop(self.queue.dequeue().get_key())
            node = Node(key, value)
            self.cache[key] = node

        self.queue.enqueue(self.cache[key])


# test cases below:

our_cache = LRUCache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1) == 1)
# returns True, was found
print(our_cache.get(2) == 2)
# returns True, was found
print(our_cache.get(2000) == 2000)
# returns False, not found
print(our_cache.get('') == '')
# returns False, not found
print(our_cache.get(None) is None)
# returns False, not found

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(2) == 2)
# returns True, was fount
print(our_cache.get(3) == 3)
# returns False, no longer found

our_cache = LRUCache(0)
our_cache.set(1, 1)
# unable to add since its capacity is 0
