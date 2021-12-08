def minimum(x):
    min=x[0]
    for i in range(len(x)):
        if(x[i]<min):
            min=x[i]
    return min

def selection_sort(x):
    lst=[]
    for i in range(len(x)):
        a=minimum(x)
        lst.append(a)
        x.remove(a)
    return lst


lst=list(map(int,input("Enter the numbers : ").split()))
sorting=selection_sort(lst)
print(sorting)