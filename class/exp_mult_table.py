# Generate and print the multiplication table (up to 10) for a given number
num = int(input('Give me a number: '))
for _ in range(1, 11):
    mult = num*_
    print(f'{num}*{_}={mult}')
    print(num,'*',_,'=',mult)