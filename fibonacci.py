#To find given number is in fibonacci or not
n=int(input("Enter the number : "))
a=0
b=1
c=1
while(a<n):
    a=b+c
    b=c
    c=a
    if(a==n):
        print(f"{n} is an fibonacci number")
        break
else:
    print(f"{n} is not a fibonaaci number ")