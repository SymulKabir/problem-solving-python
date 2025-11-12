# Task:
# Given a list of numbers, find the sum of elements that appear only once.

# Example:
# Input: [1, 2, 2, 3, 4, 4, 5]
# Output: 1 + 3 + 5 = 9

# Hint: Use collections.Counter

def unique_number_sum(number_list):
    number_object = {}
    sum_amount = 0
    for number in number_list: 
        
        if number_object.get(number):
            number_object[number] = number_object[number] + 1
        else:
            number_object[number] = 1
            
    for number in number_list:
        if number_object.get(number) and number_object[number] < 2:
            sum_amount = sum_amount + number
    return sum_amount
input_list = [1, 2, 2, 3, 4, 4, 5]
result = unique_number_sum(input_list)

# OR

def unique_number_sum2(number_list):
    sum_amount = 0
    index = 0 
    for number in number_list:
        number_list_copy = number_list.copy() 
        number_list_copy.pop(index)
        if not number in number_list_copy:
            sum_amount = sum_amount + number
        index = index + 1
    return sum_amount
    
    
input_list = [1, 2, 2, 3, 4, 4, 5]
result = unique_number_sum2(input_list)

print("result : ", result)
 