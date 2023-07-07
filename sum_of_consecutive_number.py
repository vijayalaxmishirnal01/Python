###Sum of consecutive in prime number......
num=int(input())
arr=[]
sum=0
count=0
primes=0
if num>1:
    for i in range(2,num+2):
        for j in range(2,i):
            if i % j == 0:
                break
            else:
                arr.append(i)
def is_prime(sum):
    for i in range(2,(sum//2)+2):
        if sum % i == 0:
            return False
        else:
            return True
for i in range(0,len(arr)):
    sum=sum+arr[i]
    if sum <= num:
        if is_prime(sum):
            count=count+1
print(count)


num1=int(input())
primes1=[]
for i in range(2, num1 + 1):
    for j in range(2, i):
        if i % j == 0:
            break
        else:
            primes1.append(i)
print(primes1)

