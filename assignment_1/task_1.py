# Task: Create a script that creates a file named hello.txt, writes "Hello, Python!" into it,
# and then reads it back to display the content on the console.
# Key Concept: Use open() with mode 'w' for writing and 'r' for reading. 

import os
ROOT_FOLDER = 'files'


def create_file(file_name, file_content = ""):
    if not file_name:
        print("No filename found")

    file = open(f"{ROOT_FOLDER}/{file_name}", "w")
    file.write(file_content)
    file.close()
    return True

def read_file(file_name):
    if not os.path.exists(f"{ROOT_FOLDER}/{file_name}"):
        print("Please provide filename")
        return None
    file = open(f"{ROOT_FOLDER}/{file_name}", "r")
    content = file.read()
    return content


def make_and_show_file(file_name, file_content):
    create_file(file_name, file_content)
    result = read_file(file_name)
    return result



result = make_and_show_file("hello.txt", "Hello, Python!")

print("result -->>", result)