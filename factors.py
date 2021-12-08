n=int(input("Enter the number : "))
lst=[]
for i in range(1,n):
    if(n%i==0):
        lst.append(i)
print(lst)