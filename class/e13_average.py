"""
create a program that computes the average of a collection of values entered by the user.
The user will enter 0 as a sentinel value to indicate that no further values will be provided.
Your program should display an appropriate error message if the first value entered by the user is 0.
"""
suma = 0
cont = 0
while True:
    n = int(input('Enter a number: '))
    if n == 0:
        print('Enter another value...')
    else:
        suma += n
        cont += 1
    more = bool(int(input('Do you want give another number? SI(1) NO(0)')))
    if more:
        continue
    else:
        break

avg = suma/cont
print(f'The average is:{avg}')
