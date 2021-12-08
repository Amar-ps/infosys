def power(x,y):
    if(y==0):
        return 1
    else:
        return(x*power(x,y-1))
square=power(4,2)
print(f"The square of 4 is {square}")