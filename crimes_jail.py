num=int(input("Enter the number of cells: "))
jail={}
for i in range(num):
    cell=int(input("Enter a cell Number: "))
    no_of_crimes=int(input("Enter the no of crimes in that cell: "))
    jail[cell]=no_of_crimes
print(jail)
for x,y in jail.items():
    if(y<5):
        print("cell No:",x,"No of Crimes:",y)

