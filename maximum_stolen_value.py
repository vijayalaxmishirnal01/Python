##There are n house built in a line,each. Athief is going to seal maximum value from these house.
#but, he can't steal in two adjacent house.what a maximum stolen value Display the maximum stolen value.....
#6 5 1 7 3 8

v=list(map(int,input().split(" ")))
even=0
odd=0
for i in range(0,len(v)):
    if (v[i]%2==0):
        even+=v[i]
    else:
        odd+=v[i]
        #print(max(even,odd))
m=max(even,odd)
print(m)
