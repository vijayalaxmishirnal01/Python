def moveemptytoend(arr):
    for i in arr:
        if i==0:
            arr.remove(i)
            arr.append(i)
        return arr
    arr1=[1,0,2,4,0,6,5,9,10]
    arr2=[0,1,2,3,0,4,5,0,6]
    print(moveemptytoend(arr1))
    print(moveemptytoend(arr2))