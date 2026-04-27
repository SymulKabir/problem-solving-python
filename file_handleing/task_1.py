# Merge the content of two files input1.txt and input2.txt to a single file output.txt.

import os

def get_file_content(file_name):
    if not os.path.isfile(file_name):
        return None
    file = open(file_name)
    content = file.read()
    file.close()
    return content


def merge_two_file(file1, file2, output_file):
    content1 = get_file_content(file1)
    content2 = get_file_content(file2)
    if content1 is None:
        print(f"{file1} does not exist")
        return
    if content2 is None:
        print(f"{file2} does not exist")
        return
    output_file = open(output_file, "w+")
    output_file.write(content1 + "\n" + content2)
    output_file.seek(0)
    out_content = output_file.read()
    output_file.close()
    return out_content
    
    
result = merge_two_file("input1.txt", "input2.txt", "output.txt")
print(result)

