numbers = [1, 23, 2, 13, 3, 0]

# largest_number = max(numbers)
largest_number = 0

for number in numbers:
    if largest_number < number:
        largest_number = number

print("largest number is : ", largest_number)