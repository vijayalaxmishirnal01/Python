#WAP to simulate transactions in the atm or Bank.
a=input("Do You Want any Transcation: ")
net_amt=2000
while(a=="yes"):
    str=input()
    transcation=str.split(" ")
    type=transcation[0]

    amt=int(transcation[1])
    if (type=='D'):
        net_amt +=amt
        print(net_amt)
    elif(type=='w'):
        net_amt-=amt
        print(net_amt)
        a=input("Do you want to Continues: ")
        if(a=="no"):
            break