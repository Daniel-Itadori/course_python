"""
Implement the Collatz Conjecture: Start with a number n, and repeatedly apply the rule n → n/2 if n is even
or n → 3n + 1 if n is odd. Print the sequence until n becomes 1.
"""

n = int(input('Give me a number: '))
while True:
    if n == 1:
        print('El programa termino :).')
        break
    elif n % 2 == 0:
        n = n / 2
        print(n, end=' - ')
    else:
        n = (3 * n) + 1
        print(n, end=' - ')