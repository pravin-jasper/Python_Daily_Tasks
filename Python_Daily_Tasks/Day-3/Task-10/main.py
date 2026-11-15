a=int(input("Your Total Amount"))
if(a>1000):
    dis=(a*10)/100
    print("Discount Amount",dis)
    print("you pay amount",a-dis)
elif((a>500) and (a<=1000)):
    dis1=(a*5)/100
    print("Discount Amount",dis1)
    print("you pay amount",a-dis1)
elif((a>0) and (a<=500)):
    dis2=(a*2.5)/100
    print("Discount Amount",dis2)
    print("you pay amount",a-dis2)
