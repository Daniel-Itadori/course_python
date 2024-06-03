#print('this is a sentence')
#print('this is another sentence', end='\t')
#print(5,6,7,8,'webos', sep='|')

################################

#x = ('spam')
#while x:
#    print(x, end=' ')
#    x = x[1:]

################################

# x = 10
# while x:
#     x -= 1
#     if x % 2 == 0:
#         continue
#     print(x)

################################

#
# words = ('uno', 'dos', 'tres', 'cuatro')
# k = -len(words)
# while words:
#     print(words[k])
#     del words[k]
#     k += 1
#     print(words)


################################
# words = ('uno', 'dos', 'tres', 'cuatro')
# for index in range(0, len(words)):
#     print(words[index])
#
# print('-----------------------------------------')
#
# for letter in words:
#     print(letter)
#
# print('-----------------------------------------')
#
# for _ in words:
#     print(_)
#
# print('-----------------------------------------')
#
# for k in range(5):
#     print(k)
#
# print('-----------------------------------------')

# suma = 0
# while True:
#     num = int(input('Ingresa un número: '))
#     if num < 0:
#         print(suma)
#         break
#     else:
#         suma += num
#
# #print('-----------------------------------------')
#
# suma = 0
# while True:
#     num = int(input('Ingresa un número: '))
#     if num > 0:
#         suma += num
#     on = bool(int(input('Deseas ingresar otro número? SI(1) NO(0)')))
#     if on:
#         continue
#     else:
#         print(suma)
#         break
# print('-----------------------------------------')

# items = ['aaa', 111, (4, 5), 2.01, 3.14]
# test = [(4, 5), 3.14]
# for key in test:
#     for item in items:
#         if item == test:
#             print(f'{key} was found.')
#         else:
#             print(f'{key} was not found.')
# print('-----------------------------------------')

# seq1 = 'Mood'
# seq2 = 'Spivak'
# res = []
# for x in seq1:
#     if x in seq2:
#         res.append(x)
# print(res)

# print('-----------------------------------------')
# a, b = 2, 3
# for _ in range(5):
#     if _ == a:
#         print(_, a)
#         break
#     elif _ == b:
#         print(f'this is {b}')
#     else:
#         print('Nothing')
# print('jejeje')

# print('-----------------------------------------')

# lista = []
# while True:
#     num = int(input('Ingresa un número: '))
#     if num % 2 == 0:
#         lista.append(num)
#     con = bool(int(input('Deseas agregar otro número? SI(1) NO(0)')))
#     if not con:
#         print(lista)
#         break

# print('-----------------------------------------')

# while True:
#     password = input('Ingresa la contraseña: ')
#     if password == 'python123':
#         print('WELCOME')
#         break
#     else:
#         print('Try again...')
# print('-----------------------------------------')

# while True:
#     fac = int(input('Ingresa un número para calcular su factorial: '))
#     resul = 1
#     for _ in range(1, fac + 1):
#         resul *= _
#     print(f'{fac}! es igual a: {resul}')
#
# print('-----------------------------------------')

# import random
#
# faces = []
# for f in range(1, 7):
#     faces.append(f)
# print(faces)
#
# n = 100
# face_selected = 5
# occurrence = 0
# for _ in range(n):
#     random_face = random.choice(faces)
#     if face_selected == random_face:
#         occurrence +=1
# print(f'lA fecuencia de la cara selccionada {face_selected} en {n} tiradas, es : {occurrence}')

# print('-----------------------------------------')

# ****We use ARGUMENTS when we are CALLING a function.
# ****We use PARAMETERS when we are making a function.

complex()
#********************IMPORTANTE!!********************
#Una LIBRERIA es un conjunto de MODULOS.

# import numpy as np
# e = np.e #el PUNTO funciona como un buscador.

# print('-----------------------------------------')

# def palindrome(word):
#     tam = len(word)
#     ad = 0
#     at = -1
#     while ad <= tam-1 and at >= -tam:
#         if word[ad] == word[at]:
#             ad += 1
#             at -= 1
#         else:
#             print('Esta palabra no es un Palindromo :(')
#             break
#     if ad >= tam-1 and at <= -tam:
#         print('Esta palabra
# # print(rest) es un Palindromo :)')
# palindrome(input('Inserta una palabra:'))

# print('-----------------------------------------')

# days = ['monday', 'tuesday', 'wendnesday', 'thursday', 'friday'] #packing
# #rest, school, free = days #error
# rest, *school, free = days
# # *rest, school, free = days
#
# print(rest)
# print(school)
# print(free)

# print('-----------------------------------------')

# from random import gauss
#
# my_numbers = [gauss() for num in range (10)]
# print(my_numbers)

# print('-----------------------------------------')

import statistics

# print('-----------------------------------------')

import random

random.seed(651)
print(random.random())

print('same seed')
random.seed(651)
print(random.random())
