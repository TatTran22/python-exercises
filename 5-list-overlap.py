# Take two lists, say for example these two:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# Extras:

# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

import random

c = []
d = []
e = []

# maxLen = int(input('Give me max length of list: '))
maxLen = 10;

for i in range(0, maxLen):
    c.append(random.randint(0, 99))
    if len(d) < int(maxLen*3/4):
        d.append(random.randint(0, 99))

for val in c:
    if val in d and not val in e:
        e.append(val)

print('We have 2 random list:')
print(c)
print(d)
print('The common numbers of two list: {}'.format(e))
