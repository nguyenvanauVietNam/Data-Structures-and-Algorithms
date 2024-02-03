"""
Problem 1: Square Root of an Integer

Find the square root of the integer without using any Python library. You have to find the floor value of the square root.
For example if the given number is 16, then the answer would be 4.
If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.
The expected time complexity is O(log(n))
"""

def sqrt(number):
    if number == 0 or number == 1:
        return number

    left, right = 1, number
    result = 0

    while left <= right:
        mid = (left + right) // 2

        if mid * mid == number:
            return mid
        elif mid * mid < number:
            left = mid + 1
            result = mid
        else:
            right = mid - 1

    return result

# Test cases
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")

print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (None == sqrt(-25)) else "Fail")
print("Pass" if (None == sqrt(-1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")

#My test case randome 100 case test
import random
for _ in range(100):
    num = random.randint(1, 1000)
    result = sqrt(num)
    print(f"Pass" if result * result <= num < (result + 1) * (result + 1) else "Fail", f"for input {num}: sqrt({num}) = {result}")
