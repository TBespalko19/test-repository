# # friends = {"Bob", "Rolf", "Anne"}

# # print("Bob" in friends)

# movies_watched = {"The Matrix", "Green Book", "Her"}
# user_movie = input("Enter something you've watched recently: ")

# # print(user_movie in movies_watched)
# if user_movie in movies_watched:
#     print(f"I've eatched {user_movie} too!")
# else:
#     print("I haven't watched yet")

# number = 7
# user_input = input("Enter 'y' if you would like to play: ").lower()

# if user_input == "y":
# # if user_input in ('y', 'Y'):
#     user_number = int(input("Guess our number: "))
#     if user_number == number:
#         print("You guess correctly!")
#     # elif number - user_number in (1, -1):
#     elif abs(number - user_number) == 1:
#         print("You were off by one.")
#     else:
#         print ("Sorry, it's wrong!")

## Loop
number = 7
user_input = input("Would you like to play? (Y/n) ").lower()

# while user_input != "n":
while True:
    user_input = input("Would you like to play? (Y/n) ").lower()

    if user_input == "n":
        break
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guess correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by one.")
    else:
        print ("Sorry, it's wrong!")

    