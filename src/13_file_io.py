"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
f = open('foo.txt', 'r')
print(f.read())
f.close()
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
f = open('bar.txt', 'w+')
for i in range(3):
    f.write("bar.text created! This is line %d\r\n" % (i+1))
f.close()


# Creating an extra file for practice, not in the assignment
j = open('jam.txt', "w+")
j.write('Jamar\'s favorite foods are tacos, mac&cheese, caesar salad, buffalo chicken and pizza.\n')
j.write('he also needs to exercise a lot to make up for it... \n')
j.write('maybe even use the nutrition tracker app he helped to create ;) !')
j.close()

# appending an extra line of text
j = open('jam.txt', "a+")
j.write('\n This is an extra line appended to the list of text!')
print(j.read())
j.close()

j = open('jam.txt', 'r')
print(j.read())
j.close()