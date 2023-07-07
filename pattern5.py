#Write a program to print this number pattern..

def pattern(n):
    x=0
    for i in range(n):
        x+=1
        for j in range(i+1):
            print(x,end=" ")
            print(' ')
pattern(5)