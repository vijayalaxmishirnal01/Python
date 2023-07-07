#Hierarchical Inheritance
class A:
    def parant(self):
        print('This is Parant Class')

class B(A):
    def child1(self):
        print('This is Child1 Class')

class C(A):
    def child2(self):
        print('This is Child2 Class')

obj=B()
obj1=C()
obj.parant()
obj.child1()
obj1.parant()
obj1.child2()