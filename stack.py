class StackEX:
    def __init__(self):
        self.size=int(input('Enter size of stack:'))
        self.stack=[]
        self.top=-1
        
    def PUSH(self,val):
        if self.top==self.size-1:
            print('STACK IS OVERFLOW!!')
        else:
            self.stack.append(val)
            self.top+=1
            print('Element Pushed!!!')

    def POP(self):
        if self.top==-1:
            return -1
        else:
            self.top-=1
            return self.stack.pop()

    def SHOW(self):
        if self.top==-1:
            print('STaCK is empty')
        else:
            print('Stack elements:',end='')
            for ele in self.stack:
                print(ele,end='')
            print('\n')

s1=StackEX()
while True:
    print('1.PUSH')
    print('2.POP')
    print('3.SHOW')
    print('0.EXIT')
    ch=int(input('Enter your choice:'))
    if ch==1:
        val=int(input('Enter stack element:'))
        s1.PUSH(val)
    elif ch==2:
        val=s1.POP()
        if val==-1:
            print('STACK IS IN OVERFLOW!!!')
        else:
            print('Element Popped:',val)
    elif ch==3:
        s1.SHOW()
    elif ch==0:
        break


size=5
stack=[]
top=-1


def PUSH(param):
    pass


PUSH(10)
stack=[10]
top=0   

PUSH(20)
stack=[10,20]
top=1  

PUSH(30)
stack=[10,20,30]
top=2

PUSH(40)
stack=[10,20,30,40]
top=3   

PUSH(50)
stack=[10,20,30,40,50]
top=4 