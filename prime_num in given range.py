n1=int(input("enter the lower range : "))
n2=int(input("Enter the upper range : "))
lst=[]
for i in range(n1,n2):
    count=0
    for j in range(2,i):
        if(i%j==0):
            count=1
            break
    if(count==0):
        lst.append(i)
print(lst)