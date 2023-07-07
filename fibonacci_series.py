#count=0
#n1,n2=0,1
#if nt<=0:
#elif(nt==1):
   # print(n1)
#else:
    #while(count<nt):
        #print(n1)
       # nth=n1+n2
        #n1=n2
       # n2=nth
        #count+=1



def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
fib(10)