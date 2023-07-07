#Write a program to add two numbers and calculate the time taken the program
import time
t0=time.time()
local_time=time.ctime(t0)
print(local_time)

a=int(input('Enter first number: '))
b=int(input('Enter Second Number: '))
sum=a+b
print("Sum of two numbers is: ",sum)
t1=time.time()
local_time1=time.ctime(t1)
print(local_time1)