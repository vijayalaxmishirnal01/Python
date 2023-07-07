#Hybrid Inheritance

class A:
    def parent(self):
        print('This is Parant Class')

class B(A):
    def child1(self):
        print('This is Child1 Class')

class C(A):
    def child2(self):
        print('This is Child2 Class')

class D(B,A):
    def grandchild(self):
        print('This is Grandchild Class')

obj=D()
obj.parent()
obj.child1()


