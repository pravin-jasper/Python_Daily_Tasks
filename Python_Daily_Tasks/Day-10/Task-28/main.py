students = {
    101: {"name": "Arun", "age": 21, "mark": 85},
    102: {"name": "Rahul", "age": 22, "mark": 90}
}
print("First output")
print(students)
print("modified")
print(students[101]["name"])
students[103] = {
    "name": "Kumar",
    "age": 20,
    "mark": 88
}
students[101]["mark"] = 95
del students[102]
print(students)
