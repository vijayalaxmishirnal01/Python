class Bill:
    def __init__(self,mobno,paybill):
        self.mobno=mobno
        self.paybill=paybill

class Mobile:
    def __init__(self,servicepro,mobno,dataused,paymentmet):
        self.servicepro=servicepro
        self.mobno=mobno
        self.dataused=dataused
        self.paymentmet=paymentmet

    def calbill(self,l1):
        temp=[]
        for i in l1:
            if i.servicepro=='airtel':
                bill=11*i.dataused
                tbill=bill
                if i.paymentmet=='paytm':
                    tbill=bill-(0.1*bill)
                elif i.servicepro=='jio':
                    tbill=10*i.dataused
                    temp.append(Mobile(i.mobno,int(tbill)))
                return temp

n=int(input())
l1=[]
for i in range(n):
    servicepro=input()
    mobno=int(input())
    dataused=int(input())
    paymentmet=input()
    l1.append(Bill(servicepro,mobno,dataused,paymentmet))
    res=Mobile(',0,0,').calbill(l1)
    for i in res:
        print(i.mobno,i.paybill)