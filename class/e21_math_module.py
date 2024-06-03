# Import the math module (as you want)
import math
from math import *

# Make the Poisson distribution. The user must enter the parameters. Then print out the result
#
# lam = int(input('Ingresa el valor de lambda: '))
# X = int(input('Ingresa el valor de X: '))
# DP = ((lam^X)/())

# Make an iterable with some numbers to calculate the product of all those numbers
a = [1, 2, 3]
math.prod(a, start=1)

print(math.prod(a))
# From two iterables, calculate the sum of the product of values
a = [1, 2, 3]
b = [4, 5, 6]
# mult = []
# for _ in a:
#     for __ in b:
#         mult.append(_*__)
#         __ += 1
#         continue
#     continue
# sum = 0
# for ___ in mult:
#     sum += ___
# print(sum)
print(math.sumprod(a,b))

# Calculate the GCD of two numbers that user gives
num = []
for _ in range(2):
    num.append(int(input('give me a numer:')))


# Make the binomial distribution. The user must enter the values: n, x, p. Then print out the result



# The user enter a float number, and then the ceiling of that number must appear in the screen, as
# "the ceiling of x is y "


# Choose two functions from the math documentation to make exercises like the previous