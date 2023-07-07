#write a program to purchases maximum number of articles for gives money.

import time
t0=time.time()
local_time=time.ctime(t0)
print(local_time)
money=int(input('Enter Money: '))
articles=[4,7,9,39,40,55,20,12,14,15]
print(articles)
sort=sorted(articles)
print(sort)
x=0
count=0
for i in range(0,len(sort)):
    if(sort[i]<money):
        x=x+sort[i]
        count+=1
print("Sum of articles:",x)
print("No of articles:",count)
import time
t1=time.time()
local_time=time.ctime(t1)
print(local_time)