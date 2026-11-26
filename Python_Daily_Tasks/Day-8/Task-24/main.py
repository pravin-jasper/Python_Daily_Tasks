numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
num = 0
for i in numbers:
    if i > num:
        num = i
print("Largest number:", num)
