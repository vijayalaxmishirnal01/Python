class Base:
    def __init__(self):
        print('From Base class')
    def showBase(self):
        print('Inside the Base class')

class Derived(Base):
    def __init__(self,a,b):
        super().__init__()
        self.a=a
        self.b=b
        print('From Derived class')
    def showDerived(self):
        print('A=',self.a,'B=',self.b)

obj=Derived(10,20)
obj.showBase()
obj.showDerived()