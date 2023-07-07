arr=map(int,input().split(" "))
Larr=list(arr)
carr=[]
sarr=list(set(Larr))
for i in sarr:
    if i in Larr:
        carr.append(Larr.count(i))
for x,y in zip(sarr,carr):
    print(x,y)