input_list = input("Enter a list of number: ")
input_list = input_list.replace(" ", '').replace("[", "").replace("]", "").split(",")
print("input_list", input_list)

def find_even_odd_number(numbers):
    even_numbers = []
    odd_numbers = []

    for number in numbers:
        if not str(number).isdigit():
            continue
        formated_number= int(number)
        if formated_number % 2 == 0:
            even_numbers.append(formated_number)
        else:
            odd_numbers.append(formated_number)
    print("Even Numbers:", even_numbers)
    print("Odd Numbers:", odd_numbers)
        


find_even_odd_number(input_list)

