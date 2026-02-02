numbers = range(1, 50)
prime_numbers = []

def find_prime_number(numbers):
    for number in numbers:
        if number < 2:
            continue
        is_prime = True
        print("number ->", number) 
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(number)
            print("Prime number:", number)
    print(f"prime_numbers -> {prime_numbers}")

find_prime_number(numbers)
