employees = {
    "E101": {"name": "Arun", "salary": 25000},
    "E102": {"name": "Ravi", "salary": 30000},
    "E103": {"name": "Kumar", "salary": 35000}
}
for emp_id, details in employees.items():
    print(emp_id, details["name"], details["salary"])
print("Increase salary")
employees["E101"]["salary"] += 5000
print(employees["E101"])
