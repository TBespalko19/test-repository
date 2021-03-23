# friend_ages = {"Rolf": 24,"Adam": 30, "Anne": 27}

# print(friend_ages["Adam"])

# friend_ages["Bob"] = 20 # add or change for existing key 
# print(friend_ages)

# friends = [
#     "Rolf",
#     "Adam",
#     "Anne"

# ]

# friends = [
#     {"name": "Rolf", "age": 24},
#     {"name": "Adam", "age": 30},
#     {"name": "Anne", "age": 27}
# ]

# print(friends[1]["name"])
# print(friends[1])

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}
# for student in student_attendance:
    # print(student)
    # print(f"{student}: {student_attendance[student]}")

    # Better

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

# -- Using the `in` keyword --

if "Bob" in student_attendance:
    print(f"Bob: {student_attendance[student]}")
else:
    print("Bob isn't a student in this class!")

if "Fred" in student_attendance:
    print(f"Fred: {student_attendance[student]}")
else:
    print("Fred isn't a student in this class!")

# -- Calculate an average with `.values()` --

attendace_values = student_attendance.values()
print(sum(attendace_values) / len(attendace_values))