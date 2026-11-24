n=int(input("Enter number:"))
num=int(n/2)
for i in range(1,n+1):
    if i==1 or i==n:
          print("*"*n)
    elif i==i:
        print(" "*(num)+"*")
