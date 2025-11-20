# Write a program to take a string input and count how many vowels are in the string.

def count_vowels(input):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for charecter in input:
        if charecter.lower() in vowels:
            count = count + 1;
    return count;

input_string = input('Enter a string: ')
result = count_vowels(input_string);

print(f"In your input there are {result} vowels")


