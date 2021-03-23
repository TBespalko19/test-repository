name = "Bob"
greeting = f"Hello, {name}"

print(f"Your name is: {name}")

name = "Rolf"
greeting = f"Hello, {name}"

print(f"Hello, {name}")

name = "Vanya"
greeting = "Hello, {}"
with_name = greeting.format(name) # format function inside of greeting
with_name_two = greeting.format("Rolf")

print(with_name)
print(with_name_two)