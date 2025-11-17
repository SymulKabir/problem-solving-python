# Task:
# Check if a word or sentence is a palindrome (ignore spaces and capitalization).

# Example:
# Input: "A man a plan a canal Panama" → Output: True

# Hint: Clean the string and compare with its reverse.

def palindrome_checker(sentence):
    filter_text = sentence.replace(" ", "").lower() 
    reverse_text = filter_text[::-1]
    
    return filter_text == reverse_text;
    
    
input_text = "A man a plan a canal Panama"
output = palindrome_checker(input_text)

print("Output: ", output)