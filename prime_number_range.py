def prime_number_range():
    prime_numbers = []
    # small_number = input("Where to start the range: ")

    while True:
        small_number = input("Where to start the range: ")
        if small_number.isdigit():
            small_number = int(small_number);
            break
        print("Please enter a valid number.")
        
    while True:
        large_number = input("Where to end the range: ")
        if large_number.isdigit() and int(large_number) > small_number:
            large_number = int(large_number);
            break
        print("Please enter a valid number greater than", small_number)
        
    for num in list(range(int(small_number), int(large_number) + 1)):
        
        if num < 2 or (num % 2 == 0  or num % 3 == 0 or num % 5 == 0):
            continue
        prime_numbers.append(int(num))   
    print("prime_numbers:", prime_numbers)

prime_number_range()