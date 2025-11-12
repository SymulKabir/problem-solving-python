# Task:
# Reverse the order of words in a given sentence without reversing the words themselves.

# Example:
# Input: "Python is powerful"
# Output: "powerful is Python"

# Hint: Split and join strings.


def reverse_word():
    input_text = input("Enter your sentence: ")
    input_text = input_text.split(' ')
    reverse_text = []
    for word in input_text:
        # reverse_text.insert(0, word)
        reverse_text = [word] + reverse_text 
    reverse_text = " ".join(reverse_text) 
    return reverse_text


result = reverse_word()
print("result: ", result)