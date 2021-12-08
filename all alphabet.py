# To Check given string contains all alphabet or not
import string
a=set(string.ascii_lowercase)
n=set(input("Enter your string : ").lower())
b=a-n
b=list(b)
if(len(b)==0):
    print("The given string has all alphabet character ")
else:
    a=" , ".join(b[0:len(b)])
    print(f"{a} these alphabets are missing in given string")

