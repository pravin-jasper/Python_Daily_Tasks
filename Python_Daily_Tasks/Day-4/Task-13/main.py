cash = int(input("Enter The Amount"))
led=7
cfl=6
return_bulb=6
cflbuy=0
ledbuy=0
def buy_purchase(cash):
         purchase=cash-led
         return purchase
         print(purchase)
def return_bulb_give(cash):
         return_on=cash+return_bulb
         return return_on
while cash>=led:
    cash = buy_purchase(cash)
    ledbuy+=1
    cash = return_bulb_give(cash)
    if cash==6:
       cflbuy+=1
    if cash<=0:
        break
print("Return Bulb:",ledbuy)
print("Buy Bulb:",cflbuy)
