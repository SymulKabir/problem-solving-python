import os


def get_user_input(placeholder="Enter input:- "):
    user_input = input(placeholder)
    return user_input

def print_file_content():
    file_name = get_user_input("Enter file name:- ")
    if not file_name:
        print("No file name provided")
        return
    if not os.path.isfile(file_name):
        print("File does not exist")
        return
    file = open(file_name)
    
    
    file_content = file.read()
    index = 0
    
    for line in file_content.splitlines():
        index += 1
        print(f"line {index}:- {line}")

print_file_content()



    

    