class Student:
    def write(self):
        f=open("Student.txt","a")
        rn=int(input('Enter roll no:'))
        name=input('Enter a name:')
        result=str(rn)+'\t'+name+'\n'
        f.write(result)
        f.close()

    def read(self):
        print('Content from file:')
        f=open('Student.txt','r')
        for line in f:
            print(line)
        f.close()
s1=Student()
nos=int(input('Enter no of Student:'))
for i in range(nos):
    s1.write()

s1.read()