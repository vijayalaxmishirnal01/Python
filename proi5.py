#Update
list1=[10,20,'XYZ',20.45]
list1.insert(5,'ABC')
print(list1)

#Delete
list=[10,20,'XYZ',20.45]
del list[0]
del list[0:5]
print(list)

#Remove
list2=[10,20,'XYZ',20.45]
list2.remove('XYZ')
print(list2)

#Append
list3=[10,20,'Laxmi',20.50,40]
list3.append(20)
print(list3)

#Extend
list2=[10,20,'XYZ',20.45]
list3=[10,20,'Laxmi',20.50,40]
list2.extend(list3)
print(list2 )