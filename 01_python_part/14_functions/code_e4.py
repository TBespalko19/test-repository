# def hello():
#     print("Hello!")

# hello()

# def user_age_in_seconds():
#     user_age = int(input("Enter your age: "))
#     age_seconds = user_age * 365 * 24 * 60 * 60
#     print(f"Your age in seconds is {age_seconds}.")

# print("Welcome to the age in second program!")
# user_age_in_seconds()
# print("Goodbye!")

# friends = ["Rolf", "Bob"]

# def add_friend():
#     friend_name = input("Enter your friend name: ")
#     friends1 = friends + [friend_name]

# add_friend()
# print(friends)
friends = []

def add_friend():
    friends.append("Rolf")


add_friend()
add_friend()
add_friend()

print(friends) # [Rolf]

# Complete the function by making sure it returns 42. .
def return_42():
    # Complete function here
    return 42
    
# Create a function below, called my_function, that takes two arguments and returns the result of its two arguments multiplied together
def my_function(x, y):
    return(x * y)