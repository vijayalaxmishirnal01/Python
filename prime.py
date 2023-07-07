import time
num=int(input('Enter a Prime Number: '))
t0=time.time()
if(num>1):
    for i in range(2,num):
        if(num%2==0):
            print("It is a not prime Number.")
        else:
            print("It is a prime Number.")
            break
    else:
        print("It is a prime Number")
        t1=time.time()
        print(t1-t0)