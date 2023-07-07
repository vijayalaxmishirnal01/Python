class Emp:
    def write(self):
        f1=open("Employee.txt","a")
        id=int(input('Enter Id:'))
        name=input('Enter a Name:')
        age=int(input('Enter a Age:'))
        designation=input('Enter a Designation:')
        salary=int(input('Enter a salary:'))
        result=str(id)+'\t'+name+'\n'+str(age)+'\t'+designation+'\t'+str(salary)+'\t'
        f1.write(result)
        f1.close()

    def read(self):
        print('Content From File:')
        f1=open('Employee.txt','r')
        for line in f1:
            print(line)
        f1.close()

e1=Emp()
nos=int(input('Enter no of Employee:'))
for i in range(nos):
        e1.write()
e1.read()
