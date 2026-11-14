amount = int(input("Order Amount: "))
distance = int(input("Distance from Restaurant: "))
premium = input("Premium member yes or no")

if premium == "yes":
    if amount > 500:
        print("Final Amount", amount)
    else:
        print("sorry above 500")

elif premium == "no":
    if amount > 500:
        if distance > 7 or distance >= 3:
            print("Final Amount", amount + 60)
        elif distance<3 :
            print("Final Amount", amount + 30)
    else:
        print("sorry above 500")

else:
    print("Invalid")
