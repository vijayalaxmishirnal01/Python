#Multiple Inheritance
class A:
    def parant1(self):
        print('This is Parant1 Class')

class B:
    def parant2(self):
        print('This is Parant2 Class')


class C(A,B):
    def derived(self):
        print('This is Derived1 Class')

obj=C()
obj.parant1()
obj.parant2()
obj.derived()