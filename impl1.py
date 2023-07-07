def fact(n):
    f1=1
    for i in range(1,n+1):
        f1=f1*1
        return f1

def rev(n):
    r=0
    while(n!=0):
        rem=n%10
        r=r*10+rem
        n=n//10
        return r

def sod(n):
    s=0
    for i in range(n):
        s+=int(i)
        return s