# Task: Prompt a user to enter their name and append that name to an existing roster.txt file
# without deleting the current contents.
# Key Concept: Open the file in append mode ('a') to add data to the end of the file.

import os
ROOT_FOLDER = "./files"

def confirm_file(file_name, content=""):
    print("confirming file")
    if not os.path.exists(f"{ROOT_FOLDER}/{file_name}"):
        file = open(f"{ROOT_FOLDER}/{file_name}", "w")
        file.write(content)
        file.close()
    

def append_name(file_name, name):
    if not name or not file_name:
        print("Please provide a name and file name")
        return
    confirm_file(file_name)
    file = open(f"{ROOT_FOLDER}/{file_name}", "a")
    file.write(name + "\n")
    file.close()
    return True


def main():
    input_name = input("Please enter your name: ")
    while not input_name:
        print("Name cannot be empty. Please enter your name.")
        input_name = input("Please enter your name: ")
    append_name("roster.txt", input_name)

main()