n=input("Enter the number : ")
lst=[int(i) for i in n]
sum=0
for i in range(len(lst)):
    sum=sum+(lst[i]**3)
if(sum==int(n)):
    print(f"{n} is an armstrong number ")
else:
    print(f"{n} is not an armstrong number ")
