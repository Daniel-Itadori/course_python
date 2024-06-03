"""
(A little introduction to functions)
I'd like you to write a function that accepts two lists-of-lists of numbers and returns one list-of-lists with each of
the corresponding numbers in the two given lists-of-lists added together.

It should work something like this:

>> matrix1 = [[1, -2], [-3, 4]]
>> matrix2 = [[2, -1], [0, -1]]
>> add(matrix1, matrix2)
[[3, -3], [-3, 3]]
>> matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
>> matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
>> add(matrix1, matrix2)
[[2, -1, 3], [-3, 3, -3], [5, -6, 7]]

Try to solve this exercise without using any third-party libraries (without using pandas, for example).

"""
matrix1=[]
matrix2=[]
matrix3=[]
n=int(input('Cuántas listas tendrán tus listas: '))
for i in range(1,3):
    for j in range(1, n+1):
        l=int(input(f'Ingresa la lista #{j}, de la lista #{i}'))
        if i==1:
            matrix1.append(l)
        else:
            matrix2.append(l)
for _ in matrix1:
    for __ in matrix2:
        matrix3.append(matrix1[_]+matrix2[__])
print(matrix1)
print(matrix2)
print(matrix3)

