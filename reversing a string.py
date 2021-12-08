n=input("Enter your string : ")
lst=[i for i in n]
x=[]
for i in range(len(lst)-1,-1,-1):
    x.append(lst[i])
str="".join(x[0:len(x)])
print(str)