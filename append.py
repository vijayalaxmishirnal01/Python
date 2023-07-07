nos1=[10,20,30,40,50]
nos2=nos1[:]

nos2[4]=100
for i in range(len(nos1)):
    print(nos1[i],end=' ')
for ele in nos1:
    print(ele,end=' ')


print(nos1)
print(nos2)
