n=int(input())
l=[]
i=2
temp=n
while(i<=n):
    if n%i==0:
        l.append(i)
        n=n//i
    else:
        i+=1
print(temp-min(l))