class QueueEx:
    def __init__(self):
        self.rear=-1
        self.front=0
        self.queue=[]
        self.size=int(input('Enter the size of queue:'))

    def enqueue(self,val):
        if self.rear==self.size-1:
            print('Queue is overflow!!!')
        else:
            self.queue.append(val)
            self.rear+=1
            print('Element Enqueued!!!')

    def dequeue(self):
        if self.rear==-1:
            print('Queue is underflow!!!')
        else:
            self.queue.remove(self.queue[0])
            self.rear-=1
            print('Element Dequeued!!!')

    def show(self):
        if self.rear==-1:
            print('Queue is empty!!')
        else:
            print('Queue:',end='')
            for ele in self.queue:
                print(ele,end='')
            print('\n')


q=QueueEx()
while True:
    print('1.ENQUEUE')
    print('2.DEQUEUE')
    print('3.SHOW')
    print('0.Exit')
    ch = int(input('Enter your choice:'))
    if ch == 1:
        val = int(input('Enter element:'))
        q.enqueue(val)
    elif ch==2:
        q.dequeue()
    elif ch==3:
        q.show()
    elif ch==0:
        break
