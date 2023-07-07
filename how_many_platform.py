###HOW MANY PLATFORM IN TRAINS.....

n=int(input("Enter a platform number: "))
arr_time=list(map(int,input().split(" ")))
dep_time=list(map(int,input().split(" ")))
print(arr_time)
print(dep_time)
for i in range(1,len(arr_time)):
    platform=1
    for j in range(0,len(dep_time)):
        if arr_time[i]<=dep_time[j]:
            platform+=1
print(platform)





##@Sorted the arrival time and departure time...
n1=int(input("Enter a platform number: "))
arr_time1=list(map(int,input().split(" ")))
dep_time1=list(map(int,input().split(" ")))
arr_time1.sort()
dep_time1.sort()
print(arr_time1)
print(dep_time1)
for i in range(1,len(arr_time1)):
    platform=1
    for j in range(0,len(dep_time1)):
        if arr_time[i]<=dep_time1[j]:
            platform+=1
print(platform)

