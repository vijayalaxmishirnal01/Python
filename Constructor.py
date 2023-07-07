class Base:
    def __init__(self,a):
        print('From Base class')
        self.a=a
    def showBase(self):
        print('A=',self.a)

class Derived(Base):
    def __init__(self,a,b):
        super().__init__(a)
        self.b=b
        print('From Derived class')
    def showDerived(self):
        print('B=',self.b)

obj=Derived(10,20)
obj.showBase()
obj.showDerived()