"""
Problem 4: Dutch National Flag Problem
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
You're not allowed to use any sorting function that Python provides.
Note: O(n) does not necessarily mean single-traversal.
For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.
"""

def sort_012(input_list):
    # Initialize three pointers
    low = 0  # Pointer for 0
    mid = 0  # Pointer for 1
    high = len(input_list) - 1  # Pointer for 2

    while mid <= high:
        if input_list[mid] == 0:
            # Swap the element at mid with the element at low
            input_list[low], input_list[mid] = input_list[mid], input_list[low]
            low += 1
            mid += 1
        elif input_list[mid] == 1:
            mid += 1
        else:  # input_list[mid] == 2
            # Swap the element at mid with the element at high
            input_list[mid], input_list[high] = input_list[high], input_list[mid]
            high -= 1

    return input_list

# Test cases
def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# test case 100 case
def create_test_cases():
    test_cases = []
    
    # Test cases with 0s only
    for i in range(1, 21):
        test_cases.append([0] * i)
    
    # Test cases with 1s only
    for i in range(1, 21):
        test_cases.append([1] * i)
    
    # Test cases with 2s only
    for i in range(1, 21):
        test_cases.append([2] * i)
    
    # Random test cases
    test_cases.append([0, 1, 2])
    test_cases.append([2, 1, 0])
    test_cases.append([1, 0, 2])
    test_cases.append([1, 2, 0])
    test_cases.append([2, 0, 1])
    test_cases.append([0, 0, 0, 1, 1, 1, 2, 2, 2])
    test_cases.append([2, 2, 2, 1, 1, 1, 0, 0, 0])
    test_cases.append([1, 0, 2, 0, 1, 2, 2, 1, 0])
    
    return test_cases
#create case
test_cases = create_test_cases()
for i, test_case in enumerate(test_cases):
    print(f"Test Case {i + 1}: {test_case}")
    test_function(test_case)
#Orthercase
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,
               2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([])
