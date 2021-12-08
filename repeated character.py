n=input("Enter your string : ").lower()
count=0
lst=[]
for i in range(len(n)):
    x=n[i]
    count=0
    for j in range(i+1,len(n)):
        y=n[j]
        count=0
        if(x==y):
            count=1
        if(count==1):
            lst.append(y)
lst=list(set(lst))
a=",".join(lst[0:len(lst)])
print(f"The repeated characters are {a}")
