# Copy file content of input1.txt to a new file output.txt, but  reverse the order of lines (the ast lines becomes the first lines)

import os


def get_file_content(file_name):
    if not os.path.isfile(file_name):
        return None
    file = open(file_name)
    content = file.read()
    file.close()
    return content


def create_file(file_name, output_file):
    content = get_file_content(file_name)
    if content is None:
        print(f"{file_name} does not exist")
        return
    
    new_content = ""
    for line in content.splitlines():
        new_content = line + "\n" + new_content
        
    print("content -->", new_content)
    output_file = open(output_file, "w+")
    output_file.write(new_content)
    # output_file.seek(0)
    out_content = output_file.read()
    output_file.close()
    return out_content
    
    # return out_content
    
    
create_file("input1.txt", "output.txt")