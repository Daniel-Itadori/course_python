# Make a program that determines if a number (given by the user) is odd or even
# User's number
number = int(input('Enter a number: '))
# test if the number is odd or even
if number % 2 == 0:
# print the result
    print(f'{number} is even')
else:
    print(f'{number} is odd')
