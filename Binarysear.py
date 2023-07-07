def binarySearch(list1,search):
    list1.sort()
    index=-1
    low=0
    high=len(list1)-1
    mid=0

    while low<=high:
        mid=(low+high)//2
        if list1[mid]<search:
            low=mid+1
        elif list1[mid]>search:
            high=mid-1
        else:
            index=mid
            break

    return index
size=int(input('Enter size:'))
values=input('Enter elements:').split(' ')
list1=[]
for i in range(size):
    list1.append(int(values[i]))
search=int(input('Enter searchable element:'))
index=binarySearch(list1,search)
if index==-1:
    print('Elements is not found !!')
else:
    print('Elements is found at index',index)
