##Python voncepts Revise And Codevita Problems(String Slicing)....

str="12345"
str1="12345"*5
str2="concatenation"
substr=input("Enter the part of the string that you want to find: ")
for i in range(0,len(str2)):
    if str2[i:i+len(substr)]==substr:
        print(substr,"is found")
    #if str2[i:i+3]=='cat':
        #print("Cat is found")
print(str[3: :5],str1)
