"""
Python tuples are sort of like lists, except they're immutable and
are usually used to hold heterogenous data, as opposed to lists
which are typically used to hold homogenous data. Tuples use 
parens instead of square brackets. 

More specifically, tuples are faster than lists. If you're looking
to just define a constant set of values and that set of values 
never needs to be mutated, use a tuple instead of a list. 

Additionally, your code will be safer if you opt to "write-protect"
data that does not need to be changed. Tuples enforce immutability
automatically. 
"""

# ls = [1,2,3,4]
# tup = (1,2,3,4)
# http_error_codes = ("400", "401", "403")
# http_error_codes[2]
# ls[3] = 5

# for item in ls:
#     print(item)

# for item in tup:
#     print(item)

# Example:

import math

def dist(a, b):
    """Compute the distance between two x,y points."""
    x0, y0 = a  # Destructuring assignment
    x1, y1 = b
    
    return math.sqrt((x1 - x0)**2 + (y1 - y0)**2)

a = (2, 7)   # <-- x,y coordinates stored in tuples
b = (-14, 72)

# Prints "Distance is 66.94"
print("Distance is: {:.2f}".format(dist(a, b)))



# Write a function `print_tuple` that prints all the values in a tuple

# YOUR CODE HERE

def print_tuple(x):
    print("values: ",x)
t = (1, 2, 5, 7, 99)
# for t in print_tuple: 
#     print(len(print_tuple(t)))
print_tuple(t) # Prints 1 2 5 7 99, one per line
print('t value', print_tuple(t))
# Declare a tuple of 1 element then print it
u = (1)  # What needs to be added to make this work?
print_tuple(u,)
