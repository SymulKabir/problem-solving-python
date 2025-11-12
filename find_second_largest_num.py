# Task:
# Given a list of numbers, find the second largest distinct number.

# Example:
# Input: [10, 20, 4, 45, 99, 99]
# Output: 45

# Hint: Use set() or sorting logic.

def find_second_largest_num(number_list):
    distinct_number = list(set(number_list));
    distinct_number.sort() 
    # distinct_number.reverse() 
    return distinct_number[len(distinct_number) - 2]
    
num_list = [10, 20, 4, 45, 99, 99]

result = find_second_largest_num(num_list)

print("Result:", result)
