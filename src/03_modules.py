"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print(sys.argv[0])

# Print out the OS platform you're using:
# YOUR CODE HERE

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html
import os 
print(os.name)

import platform 
# could also just write print(os.system())
print(platform.system())
print(platform.release())
#this prints the pure version name without default and date
print(platform.python_version())
# Print out the version of Python you're using:
# YOUR CODE HERE

import sys
print(sys.version)


# Print the current process ID
# YOUR CODE HERE
print(os.getpid())


# Print the current working directory (cwd):
# YOUR CODE HERE
print(os.getcwd())

## To get the full path to the directory a Python file 
## is contained in, write this in that file:
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

# Print out your machine's login name
# YOUR CODE HERE
import getpass
print(getpass.getuser())
print(os.getlogin())
