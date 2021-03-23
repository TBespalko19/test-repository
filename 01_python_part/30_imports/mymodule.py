def divide(dividend, divisor):
    return dividend / divisor


print("mymodule.py:", __name__) ## __name__ - global variable in python that changes depending on which file you're in

# $ mymodule.py: __main__


# -- importing from a folder --

import libs.mylib

