# Task: Read a multi-line text file (e.g., data.txt) and print each line prefixed with its line
# number (e.g., "1: First line content").
# Key Concept: Use a for loop to iterate through the file object and the enumerate()
# function for the index. 

import os
ROOT_FOLDER = "./files"

def read_file(file_name):
    if not file_name:
        print("Please, prove file name")
        return
    if not os.path.exists(f"{ROOT_FOLDER}/{file_name}"):
        print("File doesn't exist")
        return

    file = open(f"{ROOT_FOLDER}/{file_name}", "r")
    content = file.read()
    return content

def iterate_file(file_name):
    content = read_file(file_name) 
    for index, line in enumerate(content.splitlines()):
        print(f"{index}: {line}")


iterate_file("data.txt")

    
