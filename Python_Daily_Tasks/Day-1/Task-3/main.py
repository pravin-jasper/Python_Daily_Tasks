age=int(input("Enter Age Number:"))
if((age<0) or (age>100)):
    print("Invalid")
elif(age<18):
    print("Not Eligble")
elif((age>18)and(age<60)):
    print("Eligble")
elif(age>60 ):
    print("Senior")
