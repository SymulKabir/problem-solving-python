# Task: Read a text file containing one integer per line. Filter these numbers and write only
# the even integers into a separate file called even_numbers.txt.
# Key Concept: Practice conditional logic while reading from one file and writing to
# another.

import os
ROOT_FOLDER = './files'

def read_file(file_name):
    if not file_name:
        print("Please provide a file name")
        return
    if not os.path.exists(f"{ROOT_FOLDER}/{file_name}"):
        print("File doesn't exist")
        return
    file = open(f"{ROOT_FOLDER}/{file_name}")
    content = file.read()
    file.close()
    return content;

def create_file(file_name, content):
    file = open(f"{ROOT_FOLDER}/{file_name}", "w")
    file.write(content)
    file.close()
    return True


def filter_even_numbers(input_file_name, output_file_name):
    content = read_file(input_file_name)
    if not content:
        return
    
    even_numbers =  ""
    content = content.replace(",", "").replace(".", "")
    words = content.split()

    for word in words:
        if word.isdigit() and int(word) % 2 == 0:
            even_numbers = f"{even_numbers} {word}"
    
    
    create_file(output_file_name, even_numbers)
    return even_numbers


filter_even_numbers("integer_and_text.txt", "even_numbers.txt")