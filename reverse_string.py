def reverse_string(string):
    if len(string) == 1:
        return string
    
    return string[-1] + reverse_string(string[:-1])



word = "Hello world"

reversed_word = reverse_string(word)

print("Original string:", word)
print("Reversed string:", reversed_word)