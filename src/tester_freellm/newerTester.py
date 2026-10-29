import json

employees = [
	(1, "Alice Johnson", "Engineering", 85000),
	(2, "Brian Lee", "Marketing", 72000),
	(3, "Carla Gomez", "Human Resources", 68000),
	(4, "David Patel", "Finance", 79000),
	(5, "Emma Chen", "Customer Support", 61000),
]
empdct = [{"salary": salary} for id,name, department, salary in employees]

print(json.dumps(empdct, indent=4))

