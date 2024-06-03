import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def let(n):
    le = []
    for _ in range(0, n):
        r = random.choice(letters)
        le.append(r)
    return le


def num(n):
    nu = []
    for _ in range(0, n):
        r = random.choice(numbers)
        nu.append(r)
    return nu


def sym(n):
    sy = []
    for _ in range(0, n):
        r = random.choice(symbols)
        sy.append(r)
    return sy


l = int(input('How many letters do you want in your password?? '))
n = int(input('How many numbers do you want in your password?? '))
s = int(input('How many symbols do you want in your password?? '))
c= let(l) + num(n) + sym(s)
random.shuffle(c)
s = ''
for _ in c:
    s += _
print(f'You new password is: {s}')