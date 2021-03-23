people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

# for name, age, profession in people:
    # print(f"Name: {name}, Age: {age}, Profession: {profession}")

    # -- Much better than this! --

for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")

    # _ not need variable, this variable is meant to be ignored
    name, _, profession = person
    print(name, profession)

    head, *tail = [1, 2, 3, 4, 5] # * collect all possible variants except 1, because is a head
    print(head)
    print(tail)

    *head, tail = [1, 2, 3, 4, 5]
    print(head)
    print(tail)