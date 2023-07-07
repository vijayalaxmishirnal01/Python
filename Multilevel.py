#Multilevel Inheritance
class A:
    def parant(self):
        print('This is Parant Class')

class B(A):
    def derived1(self):
        print('This is Derived1 Class')

class C(B):
    def derived2(self):
        print('This is Derived2 Class')


obj=C()
obj.parant()
obj.derived1()
obj.derived2()