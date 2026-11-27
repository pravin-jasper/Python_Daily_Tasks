list1=[10,20,30,40,50]
list2=[30,40,50,60,70]
print(list1)
print(list2)
for i in list1:
    for j in list2:
        if i == j:
            print(i, end=" ")