def selectionSort(arr):
    for i in range(len(arr)):
        min_pos=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_pos]:
                min_pos=j
        temp=arr[i]
        arr[i]=arr[min_pos]
        arr[min_pos]=temp

n=int(input('Enter n:'))
values=input('Enter elements:').split(' ')
arr=[]
for i in range(n):
    arr.append(int(values[i]))
selectionSort(arr)
print('Sorted array:',end='')
for ele in arr:
    print(ele,end=' ')