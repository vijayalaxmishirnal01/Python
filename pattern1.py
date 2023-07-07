n=int(input("Enter the no. of rows:"))
m=int(input("Enter the no. of columns: "))
for i in range(1,n+1):
    for j in range(m,0,-1):
        if(i==j):
            print("*",end=" ")
        else:
            print("#",end=" ")
    print()
