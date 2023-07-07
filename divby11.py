num=input('Enter a number: ')
x=0 #Sum of digits at Odd places
y=0 #sum of digits at even places
for i in range(0,len(num)):
    if(i%2)==0:
        x+=int(num[i])
    else:
        y+=int(num[i])

        if((x+y)==0 or (x-y)==11):
            print("The",num,"is divisible by 11")
        else:
            print("The",num,"is not divisible by 11")