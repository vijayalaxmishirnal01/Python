def linearSearch(list1,search):
    index=-1
    for i in range(len(list1)):
        if list1[i]== search:
            index=i
            break
    return index
size=int(input('Enter size:'))
values=input('Enter elements:').split(' ')
list1=[]
for i in range(size):
    list1.append(int(values[i]))
search=int(input('Enter searchable element:'))
index=linearSearch(list1,search)
if index==-1:
    print('Elements is not found !!')
else:
    print('Elements is found at index',index)
