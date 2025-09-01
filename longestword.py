input = input("enter a sentence:")
word = input.split()
max_len_word = len(word[0])
for i in word:
    if len(i)>max_len_word:
        max_len_word = i
print("the longest word in the sentence is:", max_len_word)
