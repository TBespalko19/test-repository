# -- Unpacking kwargs --
# def named(**kwargs): ## collect named arguments into a dictionary or they can be used in a function call
# to unpack a dictionaru into keyworld arguments.
#     print(kwargs)

# named(name="Bob", age=25)

# def named(name, age):
#     print(name, age)

# details = {"name":"Bob", "age":25}

# named(**details)


# def named(**kwargs):
#     print(kwargs)

# details = {"name":"Bob", "age":25}

# named(**details) # the same like named(name="Bob", age=25)


# -- Unpacking and repacking -

# def named(**kwargs):
#     print(kwargs)

# def print_nicely(**kwargs):
#     named(**kwargs)
#     for arg, value in kwargs.items():
#         print(f"{arg}: {value}")

# print_nicely(name="Bob", age=25)


# -- Both args and kwargs --

def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1,3,5,name="Bob", age=25)

## result (1, 3, 5) - a tuple of arguments
##        {'name': 'Bob', 'age': 25} - dictionary of arguments

## *args, **kwargs - used to accept an unlimited number of arguments

# This is normally used to accept an unlimited number of arguments and keyword arguments, such that some of them can be passed onto other functions.
# You'll frequently see things like these in Python code:

def post(url, data=None, **kwargs): # kwargs - key, world arguments
    return orequest('post', url, data=data, json=json,**kwargs)



# While the implementation is irrelevant at this stage, what it allows is for the caller of `post()` to pass arguments to `request()`.

# -- Error when unpacking --


def myfunction(**kwargs):
    print(kwargs)


myfunction(**"Bob")  # Error, must be mapping (myfunction() argument after ** must be a mapping, not str)
myfunction(**None)  # Error