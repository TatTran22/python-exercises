# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

string = str(input('Please input a string: ')).lower()
isPalindrome = True

for i, v in enumerate(string):
    if v != string[len(string) - 1 - i]:
        isPalindrome = False

print('Given string "{}" is {}palindrome'.format(
    string, "" if isPalindrome else "not "))
