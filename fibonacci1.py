lst=[]
for i in range(20):
    def fibonacci(i):
        if(i==0 or i==1):
            return i
        else:
            return(fibonacci(i-1)+fibonacci(i-2))
    a=fibonacci(i)
    lst.append(a)
print(lst)
        