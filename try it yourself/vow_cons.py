"""
In this exercise, you will create a program that reads a letter of the alphabet from the user.
If the user enters a,e,i,o or u then your program should display a message indicating that the entered letter is a vowel
If the user enters y then your program should display a message indicating that sometimes y is a vowel, and sometimes y
is a consonant. Otherwise, your program should display a message indicating that the letter is a consonant.
"""
while True:
    le = input('Ingresa una letra: ')
    if le == 'a' or le == 'e' or le == ' i' or le == 'o' or le == 'u' or le == 'y':
        if le == 'y':
            print('La letra ingresada es una VOCAL y en ocasiones una CONSONANTE también.')

        else:
            print('La letra ingresada es una VOCAL.')
    else:
        print('La letra ingresada es una CONSONANTE.')