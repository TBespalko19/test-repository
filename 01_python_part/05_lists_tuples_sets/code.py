l = ["Bob", "Rolf", "Anne"] # lists
t = ("Bob", "Rolf", "Anne") # tuple - can't modify (add or remove) the tuple
s = {"Bob", "Rolf", "Anne"} # couldn't have duplicate elements

print(l[0]) # subscribed notation [0]
print(t[2])

l[0] = "Smith"
print(l)

l.append("Smith")
print(l)

# Create a list, called my_list, with three numbers. The total of the numbers added together should be 100.
my_list = [100, 0, 0]

# Create a tuple, called my_tuple, with a single value in it
my_tuple = 1,

# Modify set2 so that set1.intersection(set2) returns {5, 77, 9, 12}
set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5, 77, 9, 12}