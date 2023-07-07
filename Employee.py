class Employee:
    def insertData(self):
        id = int(input('\n Enter Emp ID:'))
        name = input('Enter Emp Name:')
        age = int(input('Enter a Age:'))
        designation = input('Enter a Designation:')
        salary = int(input('Enter a Salary:'))

        f=open("Employee.txt","a")
        result=str(id)+'\t'+name+'\t'+str(age)+'\t'+designation+'\t'+str(salary)+'\n'
        f.write(result)
        f.close()

    def showData(self):
        print("Employee Details!!!!")
        print("Id\t Name\t Age\t Designation\t Salary")
        f=open("Employee.txt","r")
        for i in  f:
            print(i+"\n")
        f.close()

obj=Employee()
print('Employee Data base!!!.')
ch=int(input('Enter a Choice:'))
while True:
    if(ch==1):
        obj.insertData()
        break
    elif(ch==2):
        obj.showData()
        break
    elif(ch==3):
        exit()