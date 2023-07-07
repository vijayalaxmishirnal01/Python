class Demo:
    def write(self):
        f=open('demo.txt','a')
        f.write('Python is Awesome')
        f.write('Python Support for OOPs')
        f.close()
        print('Data Written to the file!!')


d1=Demo()
d1.write()