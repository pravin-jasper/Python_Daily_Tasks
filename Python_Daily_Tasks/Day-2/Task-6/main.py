print("1.Bike")
print("2.Car")
print("3.Suv")
a=int(input("Enter Type Vehcile"))
b=int(input("Enter Hours:"))
if(a==1):
    if(b>8):
        print("Full Day Parking")
    elif(b<5):
        print("Paid Amount 60:",a,"Hours")
    elif((b>2) and (b<=5)):
        print("Paid Amount 40:",a,"Hours")
    elif(b<2):
        print("Paid Amount 20:",a,"Hours")

if(a==2):
    if(b>8):
        print("Full Day Parking")
    elif(b<5):
        print("Paid Amount 120:",a,"Hours")
    elif((b>2) and (b<=5)):
        print("Paid Amount 80:",a,"Hours")
    elif(b>2):
        print("Paid Amount 40:",a,"Hours")

if(a==3):
    if(b>8):
        print("Full Day Parking")
    elif(b<5):
        print("Paid Amount 150:",a,"Hours")
    elif((b>2) and (b<=5)):
        print("Paid Amount 100:",a,"Hours")
    elif(b<2):
        print("Paid Amount 60:",a,"Hours")
