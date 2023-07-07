from math import*

def square_root(n):
    a=sqrt(n)
    return a

x=int(input('Enter a Interger Number:'))
if(x>0):
    b=square_root(x)
    print("The Square Root Of:",x,"is",b)
else:
    print("The Square Root of:",x,"is complex",b)


