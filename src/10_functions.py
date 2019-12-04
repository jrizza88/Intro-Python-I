# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def is_even(x):
    if int(x) % 2 == 0:
        print(f'yes, {x} is an even number!')
        print('Even!')
        return True
    elif int(x) % 2 != 0:
        print(f'sorry, {x} is not an even number.')
        print('Odd')
        return False

# print(f'printing even number: {is_even(3)}')

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
if is_even(num):
    print(num)


