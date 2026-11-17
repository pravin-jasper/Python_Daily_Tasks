print("1.Addtion")
print("2.Substraction")
print("3.Multiplaction")
print("4.Divson")
print("5.Module")
print("6.Floor Divison")
commper=int(input("Enter your Option:"))
a=int(input("Enter the First Number:"))
b=int(input("Enter the First Number:"))
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
def flo(a,b):
    return a//b
if(commper==1):
    print("Addtion: ",add(a,b))
elif(commper==2):
    print("Substaction:",sub(a,b))
elif(commper==3):
    print("Multiplaction: ",mul(a,b))
elif(commper==4):
    print("Divison: ",div(a,b))
elif(commper==5):
    print("Module: ",mod(a,b))
elif(commper==6):
    print("Floor Divson",flo(a,b))
else:
    print("Invalid")
