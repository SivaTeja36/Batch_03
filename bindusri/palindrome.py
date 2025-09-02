a = input("enter a word: ")
rev_str=""
for i in a:
    rev_str=i+rev_str
if rev_str==a:
    print("palindrome")
else:
    print("not a palindrome")