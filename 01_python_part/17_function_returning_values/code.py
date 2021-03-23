# def add(x, y):
#     print(x + y)

# add(5, 8)
# result = add(5, 8)
# print(result) # no value, missing value, undeclared value

# def add(x, y):
#     return
#     print(x + y)
#     return x + y

# result = add(5, 8)
# print(result) 

def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor # not used different types of data for return1 and return2
    else:
        return "You full!"

result = divide(15, 0) * 5
print(result)