text = "python is great and python is easy"
word_count = {}


def handle_word_count():
    text_list = text.split(" ")
    print("text_list --->>>>", text_list)
    for word in text_list:
        if word_count.get(word):
            word_count[word] = word_count[word] + 1;
        else:
            print(f"word is in else {word}")
            word_count[word] = 1 






handle_word_count()