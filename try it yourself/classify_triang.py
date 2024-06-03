"""
A triangle can be classified based on the lengths of its sides as equilateral, isosceles or scalene.
All three sides of an equilateral triangle have the same length.
An isosceles triangle has two sides that are the same length, and a third side that is a different length.
If all sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of the three sides of a triangle from the user. Then display a message that
states the triangle’stype.
"""
while True:
    side1 = int(input('Ingresa la medida (en cm) del primer lado del triángulo:'))
    side2 = int(input('Ingresa la medida (en cm) del segundo lado del triángulo:'))
    side3 = int(input('Ingresa la medida (en cm) del tercer lado del triángulo:'))
    if side1 == side2:
        if side1 == side3:
            print('Según los datos ingresados el triángulo es EQUILATERO.')
        else:
            print('Según los datos ingresados el triángulo es ISOSCELES.')
    elif side1 == side3 or side2 == side3:
        print('Según los datos ingresados el triángulo es ISOSCELES.')
    else:
        print('Según los datos ingresados el triángulo es ESCALENO.')