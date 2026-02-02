text = "Hello i'm symul, i'm working last 30 hour to enhanced my programming skills";
vowels = 'aeiou';
vowel_count = 0;
consonant_count = 0;


for char in text:
    if char.isalpha():
        if char.lower() in vowels:
            vowel_count = vowel_count + 1;
        else:
            consonant_count = consonant_count + 1;
            
            
print({
    "vowel_count": vowel_count,
    "consonant_count": consonant_count
})