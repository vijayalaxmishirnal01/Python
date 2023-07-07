####Rotation Of List

n=int(input(" "))
l=list(map(int,input().split(" ")))
print("Original List:"+str(l))
l=[l[(i+n)%len(l)]for i,x in enumerate(l)]
print("Left rotation of list:"+str(l))
l=[l[(i-n)%len(l)]for i,x in enumerate(l)]
print("Right rotation of list:"+str(l))
