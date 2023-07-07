num=int(input("Enter the number of students: "))
l=[]
sports={}
for i in range(num):
    roll_no=int(input("Enter the roll_no of Student: "))
    interest=int(input("Enter the Number of Interest: "))
    for j in range(interest):
        sport_name=input("Enter the Sport name: ")
        l.append(sport_name)
        sports[roll_no]=l
        print(sports)
        l=list()
