# Task:
# Given numbers from 1 to n with one missing, find the missing number.

# Example:
# Input: [1, 2, 3, 5, 6]
# Output: 4

# Hint: Use formula n*(n+1)/2 or XOR trick.

def find_missing_number(numbers):
    n = len(numbers) + 1
    total = n * (n + 1) // 2
    return total - sum(numbers)

nums = [1, 3, 4, 5, 6]
print("Missing number:", find_missing_number(nums))

 