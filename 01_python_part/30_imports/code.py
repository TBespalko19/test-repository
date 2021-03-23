# -- importing specific thing from another file --

from mymodule import divide ## mymodule - file that we wanna import from; divide - thing that we wanna import

print(divide(10, 2))

## $ mymodule.py: mymodule
## 5.0


# -- __name__ --

print(__name__)  ## $ __main__

# -- importing with names --

import mymodule

mymodule.divide

print("code.py: ", __name__) ## code.py:  __main__

# How does Python know where `mymodule` is?
# Answer, it looks at the paths in sys.path in order:

# import sysa ## $ When has not correct name (added one not need a) ModuleNotFoundError: No module named 'sysa'

import sys

print(sys.path) ## $ ['/home/tania/Desktop/cource_Authomating/30_imports', '/usr/lib/python38.zip', '/usr/lib/python3.8', '/usr/lib/python3.8/lib-dynload', '/usr/local/lib/python3.8/dist-packages', '/usr/lib/python3/dist-packages']

# The first path is the folder containing the file that you ran.
# The second path is the environment variable PYTHONPATH, if it is set.
## $ export PYTHONPATH=/Users in console
## has result ## $ ['/home/tania/Desktop/cource_Authomating/30_imports', '/Users', '/usr/lib/python38.zip', '/usr/lib/python3.8', '/usr/lib/python3.8/lib-dynload', '/usr/local/lib/python3.8/dist-packages', '/usr/lib/python3/dist-packages']
# We won't cover environment variables in depth here, but they are variables you can set in your operating system. It can help Python find things to import when the folder structure is ambiguous.

# -- circular imports --
# Make mymodule.py import code.py as well.

# -- importing from a folder --

# import mymodule

print("code.py: ", __name__)

# import sys

print(sys.modules)