"""
Write a lambda function that calculates the roots of a quadratic equation ax^2+bx+c=0.
Assume that the discriminant is always non-negative.
"""
# def lambdaf(a, b, c):
#     root1 = (-b+pow((b**2)-(4*a*c), 0.5))/2*a
#     root2 = (-b-pow((b**2)-(4*a*c), 0.5))/2*a
#     print(f'las raices son: {root1} y {root2}')
# lambdaf(2,2,0)

roots = lambda a, b, c: (((-b+pow((b**2)-4*a*c, 1/2))/(2*a)),((-b-pow((b**2)-4*a*c, 1/2))/(2*a)))
print(roots(2, 2, 0))
