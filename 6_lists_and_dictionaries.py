# -------- 6. Lists & Dictionaries --------
skills = ["Testing", "Java", "Python"]
print("First 2 skills:", skills[:2])

projects = [
    {"name": "Login Test", "status": "Pass"},
    {"name": "Signup Test", "status": "Fail"}
]

for project in projects:
    print(f"{project['name']} => {project['status']}")