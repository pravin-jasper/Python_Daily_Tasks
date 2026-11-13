stu=int(input("Enter One subject Mark :"))
if(stu>100):
    print("Invalid")
elif((stu>90) and (stu<=100)):
    print("Grade O")
elif((stu>80) and (stu<=90)):
    print("Grade A+",stu)
elif((stu>70) and (stu<=80)):
    print("Grade A",stu)
elif((stu>60) and (stu<=70)):
    print("Grade B+",stu)
elif((stu>45) and (stu<=60)):
    print("Grade B",stu)
elif((stu>35) and (stu<=45)):
    print("Grade C",stu)
else:
    print("Work Hard",stu)
