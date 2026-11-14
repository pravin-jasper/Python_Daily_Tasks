baggage = int(input("Baggage weight in Kg : "))
domin= input("Domestic or International: ")
wheather = input("Baggage allowance (yes/no): ")
if(domin=="international"):
    if(wheather=="yes"):
        if((baggage>25) and (baggage<=30)) :
            print("International Passengers allow up to 30kg")
            print("Baggage exceds allowed ",baggage,"kg")
        elif((baggage>=15) and (baggage<=25)):
            print("International Passengers allow up to 30kg")
            print("Extra baggage charge applies increase 10 kg",baggage,"kg")
        elif baggage<15:
            print("International Passengers allow up to 30kg")
            print("Baggage Accepted",baggage,"kg")
    else:
        print("You would go")
elif(domin=="domestic"):
    if(wheather=="yes"):
        if(baggage==25):
            print("Baggage exceds allowed limit",baggage,"kg")
        elif((baggage>=15) and (baggage<=25)):
            print("Extra baggage charge applies increase 10kg",baggage,"kg")
        elif baggage<15:
            print("Baggage Accepted",baggage,"kg")
    else:
        print("You would go")
