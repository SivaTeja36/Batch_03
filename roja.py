print("hello roja")
print("roja is a developer")
s = "mom"
rev_str = ''
for i in s:
    rev_str = i + rev_str 
if rev_str == s:
    print("its palindrome")
else:
    print("its not a palindrome")
    
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return fact(n-1)*fact(n)   
num=5
print(fact(num)) 