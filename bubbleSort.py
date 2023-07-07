def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            #if arr[j]>arr[i]: DSC Order
            if arr[j]<arr[i]:
                temp=arr[j]
                arr[j]=arr[i]
                arr[i]=temp

n=int(input('Enter n:'))
values=input('Enter elements:').split(' ')
arr=[]
for i in range(n):
    arr.append(int(values[i]))
bubbleSort(arr)
print('Sorted array:',end='')
for ele in arr:
    print(ele,end=' ')