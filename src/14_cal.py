"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

# args = sys.args

c = calendar.TextCalendar()
today = datetime.today()
# month = datetime.today().month
# year = datetime.today().year
str = c.formatmonth(today.year, today.month)
print(str)

args = sys.argv
print(args)

print("Enter a calendar input")
y = int(input('Enter the year: '))
m = int(input('Enter the month: '))
while True:
  try:
    if y < 0:
      print(calendar.month(today.year,m))
    elif(m < 0 or m > 12):
      print('You must enter months in integer format! Nothing less than 0 or more than 13!!')
    else:
      print(calendar.month(y,m))
      print('Usage:\ncalendar.py month [year]')
  # Except not printing the designated valueerror message for some reason
  except ValueError:
    print('please enter choice as a number!')

