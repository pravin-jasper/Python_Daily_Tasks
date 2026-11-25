rows = int(input("Enter number: "))
for i in range(rows):
    if i == 0:
        print(" " * rows + "*")
    elif i == rows // 2:
        print(" " * (rows - i) + "*" * rows)
    else:
        print(" " * (rows - i) + "*" +
              " " * (2 * i - 1) + "*")
