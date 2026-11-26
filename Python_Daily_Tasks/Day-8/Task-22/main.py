n=int(input("Enter Number:"))
lst=[]
for i in range(n):
    value=int(input("enter element:"))
    lst.append(value)
lst.sort()
print(lst)
print(lst[-2])