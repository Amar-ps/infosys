def reverse(n):
    lst=[i for i in n]
    lst1=[]
    for i in range(len(lst)-1,-1,-1):
        lst1.append(lst[i])
    a="".join(lst1[0:len(lst)])
    a=int(a)
    return a

n1=int(input("Enter the lower number : "))
n2=int(input("Enter the upper number : "))
lst=[]
for i in range(n1,(n2+1)):
    x=reverse(str(i))
    if(x==i):
        lst.append(i)
print(lst)