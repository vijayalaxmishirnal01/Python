#Staircase Problem:
# A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
# Implement a method to count how many possible ways the child can run up the stairs.

def no_of_ways(n):
    if n<=1:
        return 1
    else:
        return no_of_ways(n-1)+no_of_ways(n-2)
n=int(input('Enter the no of stairs: '))
m=no_of_ways(n)
print("The No's of Possible ways are :",m)
