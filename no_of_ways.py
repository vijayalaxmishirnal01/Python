#WAP in Number of ways 0 to N.
def no_of_ways(n):
    if n<=1:
        return 1
    else:
        return no_of_ways(n-1)+no_of_ways(n-2)
n=int(input('Enter the no of steps: '))
m=no_of_ways(n)
print("The No's of Possible ways are :",m)