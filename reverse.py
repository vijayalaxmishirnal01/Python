#Accept a number from user in int format and reverse it. e.g 2341 output 1432

n=int(input('Enter a number: '))
r=0
while n !=0:
        rem =n%10
        r=r*10+rem
        n=n//10
print("Reverse of Number:"+str(r))
