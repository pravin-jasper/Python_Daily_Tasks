amount = int(input("Enter Amount: "))
a = int(input("Enter number of 500 rupees notes: "))
b = int(input("Enter number of 100 rupees notes: "))
rupee1 = 500 * a
rupee2 = 100 * b
sumof = rupee1 + rupee2
if sumof == amount:
    print("Correct Rupees:", sumof)
else:
    print("Check Again")
    print("Calculated Amount:", sumof)
    print("Entered Amount:", amount)
