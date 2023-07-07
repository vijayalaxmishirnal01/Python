# Add any two nos without using +operator and any inBuilt functions.
a=int(input('Enter the Numbers of a: '))
b=int(input('Enter the Numbers of b: '))
def without_using_operator(a,b):
    while(b!=0):
        c=a&b
        a=a^b
        b=c<<1
    return a
print("Sum of two numbers: ",without_using_operator(a,b))