# Task:

# Sum of Even Numbers Write a Python function called sum_even_numbers that takes a list of integers as input. The function should use a loop to iterate through the list and calculate the sum of all even numbers within it. Finally, the function should return this sum.

# Example:
# Input: [2, 1, 7, 9, "3" 4, "a", 9, 4]
# Output: 2 + 4 + 4 = 10
 
def sum_even_numbers(number_list):
    even_number_sum = 0
    for number in number_list:
        if number % 2 == 0:
            even_number_sum = even_number_sum + number;
    return even_number_sum
 
while True:
    input_list = input("Enter your number list: (Exp: [1, 4, 2]) ")
    input_list = input_list.replace(" ", "").replace("[", "").replace("]", "").split(",")
    # input_list = list(map(int, input_list))
    numbers = []
    for item in input_list:
        try:
            numbers.append(int(item))
        except:
            print("")
    if len(numbers) > 1:
        input_list = numbers
        break
     
    
result = sum_even_numbers(input_list)
print("Result: ", result) 