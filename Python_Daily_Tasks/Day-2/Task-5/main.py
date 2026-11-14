a=int(input("Enter Month GB"))
b=input("5G Yes or No")
if(b=="yes" or b=="no"):
    if(a>30):
        print("Power user",a,"GB")
    elif((a>15) and (a<=30)):
        print("Heavy user",a,"GB")
    elif((a>5) and (a<=15)):
        print("Moderate user",a,"GB")
    elif((a>0) and (a<=5)):
        print("Light user",a,"GB")
else:
    print("invalid")
