def greatest(a , b, c):
    if(a>b and a >c):
        return a
    elif (b>a and b>c):
        return b
    elif( c >a and c>b):
        return c
    
a= 5
b= 95
c=15

print(greatest(a, b, c))