ra = range(1, 10,2 ) #using positional-only

# defining a function with positional argumets
def func1(value1, value2, value3, /):
    print(value1/value3 + value2)
func1(1, 5, 10)

# positional-or-keyword with a built-in
com = complex(imag=5, real=1)
com2 = complex(real=1, imag=5)
com3 = (5, 4)
com4 = complex(imag = 10)

# Defining a function with positional-or-keyword
def func2(r,i=0):
    print(f'{r},{i}j')

func2(8)

# Keyword-only

def func3(pos1, *, live, student=' '):
    print(live + student + str(pos1))
func3(5, live= 'true', student= 'jake')

def some(obs, k_or_guess, my_iter='20', /, thresh='1e-05', check_finite='true', *, seed='none'):
    print(obs+k_or_guess+my_iter+thresh+check_finite+seed)
some('hola', 'adios', seed='example')

names = ['jake', 'esteban', 'fred', 'tim'] # lista
corrected_names = map(lambda name: name.title(), names) #iterator
print(list(corrected_names))

# for item in corrected_names:
#     print(item)

for item in map(lambda x, y, z: 2*x**y+z**x,
                [1, 2, 3],
                [0.1, 0.2, 0.3],
                [3, 2, 1]):
    print(item)

