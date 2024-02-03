"""
Problem 1: LRU Cache

Least Recently Used Cache
We have briefly discussed caching as part of a practice problem while studying hash maps.

The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.

While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If, however, the entry is not found, it is known as a cache miss.

When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element. After removing an element, we use the put() operation to insert the new element. The remove operation should also be fast.

For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both get and set operations as an use operation.

Your job is to use an appropriate data structure(s) to implement the cache.

In case of a cache hit, your get() operation should return the appropriate value.
In case of a cache miss, your get() should return -1.
While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first and then insert the element.
All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5.
"""

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity=5):
        if capacity <= 0:
            raise ValueError("Error: Cache capacity must be greater than 0.")
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            # Move the accessed key to the end of the OrderedDict to represent it as the most recently used.
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        return -1

    def set(self, key, value):
        if key in self.cache:
            # If the key already exists in the cache, update the value and move it to the end.
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            # If the cache is full, remove the first item (least recently used).
            self.cache.popitem(last=False)
        self.cache[key] = value

# Create a cache with a capacity of 5
our_cache = LRUCache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print("\nTest #1...")
print(" #returns 1 - our_cache.get(1):", our_cache.get(1))
print("#returns 2 - our_cache.get(2):", our_cache.get(2))
print("#returns -1 - our_cache.get(9):", our_cache.get(9))

our_cache.set(5,6)
our_cache.set(6,6)

print("#Returns 5 - our_cache.get(5):", our_cache.get(5))
print("#Returns 6 - our_cache.get(6):", our_cache.get(6))

# Create a new cache with a different size
our_new_cache = LRUCache(2)
our_new_cache.set(1, 1)
our_new_cache.set(2, 2)
our_new_cache.set(1, 10)
print("\nTest #2...")
print("#Returns 10 :", our_new_cache.get(1))
print("#Returns 2:", our_new_cache.get(2))

# Create another cache with a size of 0
try:
    another_new_cache = LRUCache(0)
    print("\nTest #3...")
    print("Capacity of cache is ", another_new_cache.capacity)

    # Should raise an exception
    another_new_cache.set(1, 1)
except ValueError as ve:
    print(ve)
print("another_new_cache :", another_new_cache.get(1))


