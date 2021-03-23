# numbers = [1, 3, 5]
# # doubled = []

# # for num in numbers:
# #     doubled.append(num * 2)

# #     print(doubled)

# doubled = [x * 2 for x in numbers]
# print(doubled)

friends = ["Bob", "Rolf", "Anne", "Jen", "Samantha", "Saurabh"]
# starts_s = []

# for friend in friends:
#     if friend. startswith("S"):
#         starts_s.append(friend)
#         print(starts_s)

starts_s = [friend for friend in friends if friend.startswith("S")]
# starts_s = friends
print(starts_s)
print("friends: ", id(friends), "starts_s: ", id(starts_s))
