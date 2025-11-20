numbers = [4, 2, 5, 1, 3]

def sort_numbers(numbers):
    sorted_numbers = []
    for number in numbers:
        if len(sorted_numbers) != 0 and  sorted_numbers[0] < number < sorted_numbers[len(sorted_numbers) - 1]:
            index = 0
            for item in sorted_numbers:
                if item > number:
                    sorted_numbers.insert(index, number)
                    break
                index = index + 1
        elif len(sorted_numbers) and sorted_numbers[0] >= number:
            sorted_numbers.insert(0, number)
        elif len(sorted_numbers) and sorted_numbers[len(sorted_numbers) - 1] <= number:
            sorted_numbers.append(number)
        else:
            sorted_numbers.append(number)
    return sorted_numbers
                
                
result = sort_numbers(numbers)
print(f"The sorted numbers are: {result}")


def sort_numbers2(numbers):
    current_list = numbers.copy()
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            numbers[i] = current_list[i + 1]
            numbers[i + 1] = current_list[i]
            sort_numbers2(numbers)
            break
    return numbers


# result = sort_numbers2(numbers)
# print(f"The sorted numbers are: {result}")