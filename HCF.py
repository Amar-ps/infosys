n1=int(input("Enter the first number : "))
n2=int(input("Enter the second number : "))
lst1=[]
lst2=[]
for i in range(1,n1):
    if(n1%i==0):
        lst1.append(i)
for i in range(1,n2):
    if(n2%i==0):
        lst2.append(i)
lst1=set(lst1)
st=lst1.intersection(set(lst2))
st=list(st)
print(f"The HCF of {n1} and {n2} is {max(st)}")