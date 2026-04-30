students = [("Ali", 85), ("Dina", 92), ("Mira", 78)]

sorted_students = sorted(students, key=lambda x: x[1], reverse=True)

print(sorted_students)
