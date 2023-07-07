import pymysql

def insert():
    print('### INSERT OPERATION ###')
    rn=int(input('Enter a rollno:'))
    name=input('Enter a Name:')
    mob=input('Enter Mobile NO:')
    email=input('Enter a Email:')
    add=input('Enter a Address:')
    marks=input('Enter a Marks:')

    con=pymysql.connect(host='127.0.0.1',user='root',password='',database='erp',port=3306)
    cur=con.cursor()

    sql='INSERT INTO student (Rollno,Name,Mobileno,Email,Address,Marks)VALUES(%s,%s,%s,%s,%s,%s)'
    values=(str(rn),name,mob,email,add,str(marks))
    cur.execute(sql,values)
    con.commit()
    print('One row Inserted successful !!!')
    con.close()

while True:
    print('1.INSERT')
    print('2.UPDATE')
    print('3.DELETE')
    print('4.SELECT')
    print('0.EXIT')
    choice=int(input('Enter Your choice:'))
    if choice==1:
        insert()
    elif choice==0:
        break
    #elif choice==2:
        #update():
    #elif choice==2:
       #delete():
    #elif choice==2:
       # select():


