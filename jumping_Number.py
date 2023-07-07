#Enter a Number:78261831  Sum of even nos:8+2+6+9=25  Sum of odd nos:7+1+3+1=12

no=input('Enter a Number: ')
esum=0
osum=0
for i in no:
    if int(i)%2==0:
        esum=esum+int(i)
    else:
        osum=osum+int(i)
print("Sum of Even No: ",esum)
print("Sum of Odd No: ",osum)
