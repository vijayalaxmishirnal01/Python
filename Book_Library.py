class Book:
    def __init__(self,bid,bname):
        self.bid=bid
        self.bname=bname

class Library:
    def __init__(self,lid,address,book_list):
        self.lid=lid
        self.address=address
        self.book_list=book_list
    def count_of_book(self,character):
        count=0
        for i in self.book_list:
            if i.bname[0]==character:
                count+=1
        return  count
    def remove_book(self,l1):
        for i in l1:
            for j in self.book_list:
                if j.bname==i:
                    self.book_list.remove(j)

n=int(input())
objs=[]
for i in range(n):
    bid=input()
    bname=input()
    objs.append(Book(bid,bname))
lid=int(input())
address=input()
book_list=input()

ch=input()
l=Library(lid,address,book_list)
n1=int(input())
l1=[]
for i in range(n1):
    name=input()
    l1.append(name)

print(l.count_of_book(ch))
l.remove_book(l1)
for i in l.book_list:
    print(i.book_name)

