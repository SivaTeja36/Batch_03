str1 = input("enter a word:").replace(" ","").lower()
str2 = input("enter a word:").replace(" ","").lower()
if len(str1) != len(str2):
    print("they are not anagrams as their lenght is not equal")
else:
    count1 = {}
    count2 = {}
    for ch in str1:
        count1[ch] = count1.get(ch,0)+1
    for ch in str2:
        count2[ch] = count2.get(ch,0)+1
    if count1 == count2:
        print("yes! they are anagrams")
    else:
        print("no! they are not anagrams")