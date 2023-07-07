##There is a train 1 to N are Seats Number....

s=int(input("Enter a Train Seat Number: "))
if(s % 12 == 1):
    print(str(s + 11) + "WS")
elif(s % 12 == 2):
    print(str(s + 9) + "MS")
elif (s % 12 == 3):
    print(str(s + 7) + "AS")
elif (s % 12 == 4):
    print(str(s + 5) + "AS")
elif (s % 12 == 5):
    print(str(s + 3) + "MS")
elif (s % 12 == 6):
    print(str(s + 1) + "WS")
elif(s % 12 == 7):
    print(str(s + 11) + "WS")
elif(s % 12 == 8):
    print(str(s + 9) + "MS")
elif (s % 12 == 9):
    print(str(s + 7) + "AS")
elif (s % 12 == 10):
    print(str(s + 5) + "AS")
elif (s % 12 == 11):
    print(str(s + 3) + "MS")
elif (s % 12 == 12):
    print(str(s + 1) + "WS")