# name = input("Enter your name: ")
# surname = input("Enter your surname: ")
# age = input("Enter your age: ")

# print(name)
# print(surname)
# print(age)

size_input = input("How big is your house (in square feet): ")
square_feet = int(size_input)
square_metres = square_feet / 10.8

print(square_metres)
print(f"{square_feet} square feet is {square_metres:.2f} square metres.")
