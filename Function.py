import math;

def addno(a,b):
    result = a+b
    print('Addition',result)

def subno(a,b):
    result = a-b
    print('Substration',result)

def multino(a,b):
    result = a*b
    print('Multiplication',result)

def swapno(a,b):
    temp=a
    a=b
    b=temp
    print('a=',a,'b=',b)

def expno(n):
    exponent=4
    print('Expontial value is:', math.exp(exponent))

def floatno(a,b):
    result=a/b
    print('FloatDivision:',result)

def intno(a,b):
    result=a//b
    print('IntergerDivision:',result)

def rem(a,b):
    result = a%b
    print('Remainder is:',result)

while True:
    print('1.Addition:')
    print('2.Subtraction:')
    print('3.Multiplication:')
    print('4.Swapping:')
    print('5.Expontial:')
    print('6.FloatDivision')
    print('7.IntegerDivision:')
    print('8.Remainder:')
    print('9.Exit.')

    ch=int(input('Enter choice:'))
    if ch==1:
        a=int(input('Enter a:'))
        b=int(input('Enter b:'))
        addno(a,b)

    elif ch == 2:
            a = int(input('Enter a:'))
            b = int(input('Enter b:'))
            subno(a, b)

    elif ch==3:
        a=int(input('Enter a:'))
        b=int(input('Enter b:'))
        multino(a,b)

    elif ch==4:
        a=int(input('Enter a:'))
        b=int(input('Enter b:'))
        swapno(a,b)

    elif ch==5:
        n=int(input('Enter n:'))
        expno(n)

    elif ch==6:
        a=int(input('Enter a:'))
        b=int(input('Enter b:'))
        floatno(a,b)

    elif ch==7:
        a=int(input('Enter a:'))
        b=int(input('Enter b:'))
        intno(a,b)

    elif ch==8:
        a=int(input('Enter a:'))
        b=int(input('Enter b:'))
        rem(a,b)

    elif ch==9:
        break