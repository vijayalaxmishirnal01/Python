# Super Inheritance

class Base:
    def __init__(self):
        print('From Base class')
    def showBase(self):
        print('Inside base class')

class Derived(Base):
    def __init__(self):
        super().__init__()
        print('From Derived class')
    def showDerived(self):
        print('Inside Derived Class')
obj=Derived()