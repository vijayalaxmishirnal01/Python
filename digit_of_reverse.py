def revno(no6):
    i_digit=0
    i_rev=0
    while(no6!=0):
        i_digit=no6%10
        i_rev=(i_rev*10)+i_digit
        no6=no6//10

    return i_rev
no3=int(input('enter a number: '))
print("The Original no is:",no3)
res=revno(no3)
print("The Reveresed Number is: ",res)