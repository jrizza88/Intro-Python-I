# define a doubling function that passes args by value
def double(x):
    x = x * 2
    return x
# print(double(10))
# define a doubling function that passes args by reference
num = 10
print(double(num))
print(num)


# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(num):
    if num % 2 == 0:
        print('true number was even')
        return True
    elif num % 2 != 0:
        print('false, number not even')
        return False
    else: 
        if num == str(num):
            print('please enter an integer!')

  
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

if is_even(num):
    print(num)
