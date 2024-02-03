"""
Problem 6: Unsorted Integer Array
Max and Min in a Unsorted Array
In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?
"""


def get_min_max(ints):
    if not ints:
        return None

    min_val = max_val = ints[0]

    for num in ints:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num

    return (min_val, max_val)

### Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
#Orthercase
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print("Pass" if ((2, 2) == get_min_max([2])) else "Fail")
print("Pass" if ((-1, 1) == get_min_max([1, -1])) else "Fail")
print("Pass" if ((None, None) == get_min_max([])) else "Fail")