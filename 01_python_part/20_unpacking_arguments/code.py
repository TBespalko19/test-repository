def multiply(*args): # collect the agruments
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total

# print(multiply(1, 3, 5))

# def add(x, y):
#     return x + y

# nums = [3, 5]
# print(add(*nums))

# nums = {"x": 15, "y": 25}
# # print(add(x=3, y=5))
# # print(add(x=nums["x"], y=nums["y"])) == 
# print(add(**nums))

def apply(*args, operator): # operator - compulsory or required named argument
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."

print(apply(1, 3, 6, 7, operator="+"))
print(apply(1, 3, 6, 7, operator="*"))
