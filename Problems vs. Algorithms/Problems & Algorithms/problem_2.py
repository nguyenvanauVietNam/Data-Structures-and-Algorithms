"""
Problem 2: Search in a Rotated Sorted Array

You are given a sorted array which is rotated at some random pivot point.
Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]
You are given a target value to search. If found in the array return its index, otherwise return -1.
You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).
"""

def rotated_array_search(input_list, number):
    left, right = 0, len(input_list) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if input_list[mid] == number:
            return mid
        
        # Check if the left half is sorted
        if input_list[left] <= input_list[mid]:
            if input_list[left] <= number < input_list[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Otherwise, the right half must be sorted
        else:
            if input_list[mid] < number <= input_list[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])


# test case
import random

for _ in range(100):
    input_list = sorted(random.sample(range(1, 101), 10))
    pivot = random.randint(0, 9)
    rotated_list = input_list[pivot:] + input_list[:pivot]
    number = random.randint(1, 100)
    result_linear_search = linear_search(rotated_list, number)
    result_rotated_search = rotated_array_search(rotated_list, number)
    if result_linear_search == result_rotated_search:
        print(f"Pass: Target {number} found at index {result_linear_search}")
    else:
        print(f"Fail: Target {number} not found as expected")
#Orthercase
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], -1])