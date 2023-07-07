###Sum of consecutive in prime number......

n=int(input("Enter a no.: "))
primes=[]
for i in range(2,n+1):
    for j in range(2,i):
        if i%j == 0:
            break
        else:
            primes.append(i)
print(primes)


count=0
n1=int(input("Enter a number: "))
primes1=[i for i in range(2,n1+1) if all (i%j!=0 for j in range(2,int(i**0.5)+1))]
print(primes1)
for i in range(2,len(primes1)):
    sum=0
    for j in primes1:
        sum=sum+j
        if(sum==primes1[i]):
            count+=1
            break
        if(sum>primes1[i]):
            break
print(count)
