"""list=['q','a','t','d','o','f','e']
list1=['a','e','i','o','u']
result=[i for i in list for j in list1]
print(result)"""

a=("p"*2)*3
b=("p"*3)*2
print(a==b)

#Maximum guest in hour

guest_entered=[15,10,12,13,16]
guest_left=[8,3,10,3,8]
present_guest=list(map(lambda x,y:x-y,guest_entered,guest_left))
print(present_guest)
a=(max(present_guest))
max_index=present_guest.index(a)
print("Minimum Guest Present at",max_index+1,"hour is:",a)