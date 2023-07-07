###Find the minimum mumber of coins required to from any value between 1 to N. Both inclusive.
#1.Commulative value of the coins should not exceed N.
#2.Coin determainted are 1 rupee,2 rupee,5 rupee.

"""
i=1
while i==1:
    n=int(input())
    if n<=3:
        if n==1:
            print("1")
        else:
            print("2")
    else:
        c1,c2=0,0
        c5=(n-4)//5
        b=n*(c5*5)
        if b%2==0:
            c1=2
        else:
            c1=1
        b-=c1
        c2=b//2
        print(c1+c2+c5)
i=int(input((":::")))
"""

i=1
while i==1:
    N=int(input("Enter a number: "))
    if N <= 3:
        if N == 1:
            print("1")
        else:
            print("2")
    else:
        c1,c2=0,0
        c5=(N-4)//5
        b=N-(c5*5)
        if b is (b%2==0):
            c1=2
        else:
            c1=1
        b=b-c1
        c2=b//2
        print(c1+c2+c5)