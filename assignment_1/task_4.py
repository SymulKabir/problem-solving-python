# Task: Open an existing text file, find all occurrences of a specific word (e.g., "fox"),
# replace them with another (e.g., "cat"), and save the result into a new file.
# Key Concept: Use the string.replace() method on the file content before writing it to a
# new destination.

import os
ROOT_FOLDER = "./files"

def read_file(file_name):
    if not file_name:
        print("Please, provide a filename")
        return
    if not os.path.exists(f"{ROOT_FOLDER}/{file_name}"):
        print("File doesn't exist")
        return
    file = open(f"{ROOT_FOLDER}/{file_name}", "r")
    content = file.read()
    file.close()
    return content

def replace_word_in_file(file_name, target_word, replacement_word, new_file_name):
    content = read_file(file_name)
    if not content:
        return
    modified_content = content.replace(target_word, replacement_word)

    file = open(f"{ROOT_FOLDER}/{new_file_name}", "w")
    file.write(modified_content)
    file.close()
    print(f"Replaced '{target_word}' with '{replacement_word}' and saved to '{new_file_name}'")


replace_word_in_file("fox_history.txt", "fox", "cat", "cat_history.txt")

