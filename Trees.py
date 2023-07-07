####Fruit Trees

f=list(map(int,input().split()))
s=int(input("Enetr the start position of sam's house: "))
t=int(input("Enetr the end position of sam's house: "))
a=int(input("Enter position of apple tree: "))
b=int(input("Enter position of orange tree: "))
ca=0
co=0
for i in range(1,f[0]+1):
    d=int(input("Enter a distance: "))
    if(a+d>s & a+d<=1):
        ca+=1
        if(b+d<s & b+d>=t):
            co+=1
print(ca)
print(co)