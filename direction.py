# WAP to accept direction & distance from the user Assume the user is at origin initially,
# After receiving the direction & distance from user,Display the final co-ordinates: Input:-U 10 L 5 D 5 Output:- x,y=-5,5

x = 0
y = 0
num = int(input("How Many Directions you want to move: "))
co_ordinates = {}

for i in range(num):
    dir = input("Enter Your Direction(U,D,R,L): ")
    dis = int(input("Enter your Distance in interger as(10,5,4,5): "))
    co_ordinates[dir] = dis
print(co_ordinates)

for a,b in co_ordinates.items():
    if(a=='U'):
        y=y+b
    elif(a=='D'):
        y=y-b
    elif(a=='R'):
        x=x+b
    elif(a=='L'):
        x=x-b

        print('AS per given Direction and Distance values of x and y are:',x,y)

