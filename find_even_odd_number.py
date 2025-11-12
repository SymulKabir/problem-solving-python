input_list = input("Enter a list of numbers (ex: [1, 2, 3]): ")
input_list = input_list.replace(" ", '').replace("'", '').replace('"','').replace("[", "").replace("]", "").split(",")

def find_even_odd_number(numbers):
    even_numbers = []
    odd_numbers = []

    for number in numbers:
        if not str(number).isdigit():
            continue
        formatted_number= int(number)
        if formatted_number % 2 == 0:
            even_numbers.append(formatted_number)
        else:
            odd_numbers.append(formatted_number)
    print("Even Numbers:", even_numbers)
    print("Odd Numbers:", odd_numbers)
        


find_even_odd_number(input_list)

