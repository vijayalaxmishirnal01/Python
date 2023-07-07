#Single Inheritance
class A:
    def parant(self):
        print('This is Parant Class')

class B(A):
    def child(self):
        print('This is Child Class')

obj=B()
obj.parant()
obj.child()