n1=int(input("Enter your first number : "))
n2=int(input("Enter your second number : "))

a=max(n1,n2)
while(True):
    if(a%n1==0 and a%n2==0):
        print(f"The LCM of {n1} and {n2} is {a}")
        break
    a=a+1