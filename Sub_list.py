N=int(input('Enter Size:'))
S=int(input('Enter Sum:'))

A=[]
value=input('Enter list Values:').split(' ')
for i in range(N):
    A.append(int(value[i]))
    for i in range(N):
        s1=0
        for j in range(i,N):
            if s1==S:
                print(i+1,j+1)
            elif s1>S:
                break