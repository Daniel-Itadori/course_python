"""
Positions on a chess board are identified by a letter and a number.
The letter identifies the column, while the number identifies the row,as shown here:
https://cdn2.vectorstock.com/i/1000x1000/53/21/a-chessboard-white-and-bla-vector-22415321.jpg
Write a program that reads a position from the user.
So, for example if the user enters 'a1' then your program should report that the square is black.
if the user enters 'd5' then your program should report that the square is white
"""
while True:
    p = input('Ingresa una posición para saber el color del cuadro: ')
    le = len(p)
    p1 = p[0]
    p2 = int(p[1])
    g1 = 'a', 'c', 'e', 'g'
    g2 = 'b', 'd', 'f', 'h'
    if le == 2 and 0 < p2 < 9 and (p1 in (g1 or g2)):
        if p2 % 2 == 0:
            if p1 in g1:
                print('El color del cuadro según la posición ingresada es BLANCO.')
            else:
                print('El color del cuadro según la posición ingresada es NEGRO.')
        elif p1 in g1:
            print('El color del cuadro según la posición ingresada es NEGRO.')
        else:
            print('El color del cuadro según la posición ingresada es BLANCO.')
    else:
        print('Ingresa una posición valida...')
        continue
