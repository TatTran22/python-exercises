# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


inputNumber = int(input('Give me a number: '))

print('{} is {} number'.format(inputNumber,
      'even' if inputNumber % 2 == 0 else 'odd'))

if inputNumber % 4 == 0:
    print('{} is a multiple of 4'.format(inputNumber))

num = int(input('Give number to check: '))
check = int(input('and a number to divide: '))

print('{} {}divides evenly into {}'.format(
    num, 'not ' if num % check != 0 else '', check))
