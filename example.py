##Give an array of integer ,perfom atmost k maximum operations so, that the sum of the elements of final array is minimum.arr[i] arr[i]//2

n=input().split(" ")
k=int(input("Enter a k Value:"))
val=list(map(int,input().split(" ")))
#k=int(k)
for i in range (k,0,-1):
    temp=(max(val)//2)
    val.remove(max(val))
    val.append(temp)
print(sum(val),end=" ")

print("------Minimum Operations-----")
k1=int(input("Enter a minimum operations to be perform: "))
arr_list=list(map(int,input().split(" ")))
for j in range(1,k1+1):
    max_value=max(arr_list)
    i=arr_list.index(max_value)
    arr_list.remove(max_value)
    m1=max_value//2
    arr_list.insert(j,m1)
print(sum(arr_list))

