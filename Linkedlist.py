class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next != None:
                temp=temp.next
            temp.next=new_node
        print('Node inserted successfully!!!')
    def display(self):
        print('Linked list:',end='')
        temp=self.head
        while temp is not None:
            print(temp.data,end='=>')
            temp=temp.next
        print('None')
list1=LinkedList()
while True:
    print('1.INSERT')
    print('2.Display')
    print('0.Exit')
    ch=int(input('Enter Your choice:'))
    if ch==1:
        data=int(input('Enter data:'))
        list1.insert(data)
    elif ch==2:
        list1.display()
    elif ch==3:
        break