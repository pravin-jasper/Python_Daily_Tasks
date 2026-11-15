cap = int(input("Battery Capacity: "))
current = int(input("Current Battery Percentage : "))
desired= cap+current
sub=desired-current
if((current>80) or (current<=100)):
    print("Desired :",desired)
    print("Energy Required",cap*sub/100)
elif((current>50) or (current<=80)):
    print("Desired :",desired)
    print("Energy Required",cap*sub/100)
elif((current>20) or (current<=50)):
    print("Desired :",desired)
    print("Energy Required",cap*sub/100)
elif(current>20):
    print("Desired :",desired)
    print("Energy Required",cap*sub/100)
else:
    print("Invalid")
