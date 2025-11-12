# Task:
# Find the longest word in a given sentence.

# Example:
# Input: "Python makes coding interesting"
# Output: "interesting"

# Hint: Use split() and len().

def find_longest_word(text):
    words = text.split(" ")
    longest_word = '';
    for word in words:
        if not word:
            longest_word = word
        elif len(word) > len(longest_word):
            longest_word = word
    print("Longest word: ", longest_word)


input_text = "Python makes coding interesting";
find_longest_word(input_text)
