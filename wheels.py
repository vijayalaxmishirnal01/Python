v=int(input('Enter the no of vehicles: '))
w=int(input('Enter the no of wheels in multiple of 2: '))
if(w%2==0):
    if(v<w):
        x=((4*v)-w)//2
        y=v-x
        print("No of two wheeles:",x,"and No of Four Wheeles are:",y)
    else:
        print("please enter the wheels in multiple of 2 and vehicles must be less than wheels")
