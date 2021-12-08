n1=int(input("Enter the lower range : "))
n2=int(input("Enter the upper range : "))
lst=[]
for i in range(n1,n2):
    sum=0
    i=str(i)
    l1=[int(j) for j in i]
    for k in range(len(l1)):
        sum=sum+(l1[k]**3)

    if(sum==int(i)):
        lst.append(int(i))
print(lst)
