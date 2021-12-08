#decimal to binary
n=int(input("Enter your number : "))
a=n
lst=[]
while(n):
    res=n%2
    lst.append(res)
    n=n//2
lst.reverse()
bin=[str(i) for i in lst]
binary="".join(bin[0:len(bin)])
print(f"The binary Equivalent of {a} is {binary}")


#binary to decimal
n=input("Enter the number : ")
lst=[int(i) for i in n]
lst.reverse()
number =0
for i in range(len(lst)):
    number=number+(lst[i]*(2**i))
print(number)

