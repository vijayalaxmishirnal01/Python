x=int(input(' '))
for i in range(x+1):
    if i<=10:
        print(i,end=' ')
    else:
        str1=str(i)
        a=int(str1[0])
        b=int(str1[1])
        if(a-b==1) or (a-b==-1):
            print(i,end=' ')