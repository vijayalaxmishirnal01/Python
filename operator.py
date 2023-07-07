class Time:
    def inputTime(self):
        values=input('Enter Time:').split(':')
        self.hr=int(values[0])
        self.min=int(values[1])
        self.sec=int(values[2])

    def showTime(self):
        print('Time=>',self.hr,':',self.min,':',self.sec)

    def __add__(self,t2):
        temp = Time()
        temp.sec = self.sec+t2.sec
        temp.min = self.min+t2.min
        temp.hr = self.hr+t2.hr

        if temp.sec > 60:
            temp.sec = temp.sec-60
            temp.min = temp.min+1

        if temp.min > 60:
            temp.min = temp.min-60
            temp.hr = temp.hr+1

            return temp

    def __sub__(self,t2):
        temp=Time()
        temp.sec=self.sec-t2.sec
        temp.min=self.min-t2.min
        temp.hr=self.hr-t2.hr

        return temp

t1 = Time()
t2 = Time()
t1.inputTime()
t2.inputTime()
t1.showTime()

t3 = Time()
t3 = t1+t2
print('Addition of time')
t3.showTime()
t4=Time()
t4=t1-t2 #Operator Overloading
print('Substration of time')
t4.showTime()

