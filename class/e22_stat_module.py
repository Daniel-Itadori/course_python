# Read the documentation and use the functions you want, like the previous exercise

import statistics

my_normal = statistics.NormalDist() # aquí creamos un objeto, esto es una instancia.
my_normal2 = statistics.NormalDist(2, 1)
print(my_normal2.variance)

print(my_normal.samples(5))
print(my_normal.pdf(1))
print(my_normal.cdf(1))