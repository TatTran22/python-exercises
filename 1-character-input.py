# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Extras:
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
from datetime import datetime

name = input('Tell me your name: ')
print('Hello {}'.format(name))
age = input('How old are you? ')
message = 'in {} you will be 100 years old.\n'.format(datetime.now().year + 100 - int(age))

print(message)
# Extras
times = int(input('How many time you want to print out above message? '))
print(message * times)