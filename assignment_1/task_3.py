# Task: Write a function that reads a file and returns a dictionary containing the total
# number of lines, words, and characters.
# Key Concept: Combine file reading with string methods like .split() to count words and
# len() for characters.

import os
ROOT_FOLDER = './files'

def read_file(file_name):
    if not file_name:
        print("please provide file name")
        return 

    if not os.path.exists(f"{ROOT_FOLDER}/{file_name}"):
        print("file doesn't exist")
        return
    file = open(f"{ROOT_FOLDER}/{file_name}", "r")
    content = file.read()
    file.close()
    return content

def count_file_content(file_name):
    content = read_file(file_name)
    if not content:
        return
    lines_length = len(content.splitlines())
    words_length = len(content.split())
    characters_length = len(content)


    file_statistics = {
        "lines": lines_length,
        "words": words_length,
        "characters": characters_length
    }

    return file_statistics 


result = count_file_content("data.txt")
print(result)
