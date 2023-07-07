#Write a program to multiple two numbers by sccessive addition

a=int(input('Enter First Number: '))
b=int(input('Enter Second Number: '))
mul=0
if(a>b):
    for i in range(0,b):
        mul+=a
        print(mul)
    else:
        for i in range(0,a):
            mul+=b
            print(mul)
