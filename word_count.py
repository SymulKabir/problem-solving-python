# name = input('Enter file:')
# handle = open(name, 'r')

# # counts = dict()
# counts = {}

# for line in handle:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word,0) + 1

 

# bigcount = None
# bigword = None
# for word,count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count

# print(bigword, bigcount)



name = input("Enter file name: ")
file_info = open(name, "r");

word_obj = {}
for line in file_info:
    line_list = line.split()
    
    for word in line_list:
        if word_obj.get(word):
             word_obj[word] = word_obj.get(word, 0) + 1
        else:
             word_obj[word] = 1
       
max_count_word = None        
max_count_word_number = None     

for word, count in word_obj.items():
    if max_count_word_number is None or max_count_word_number < count:
        max_count_word = word  
        max_count_word_number = count  

print("max_count=->>", max_count_word)
print("max_count_word_number=->>", max_count_word_number)
