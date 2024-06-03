

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

while True:
    yc = (input('Make a choose: r(Rock), p(Paper) or s(Scissors)')).lower()
    r = rock
    p = paper
    s = scissors
    op = [r, p, s]
    cc = random.choice(op)
    print(cc)
    if yc == 'r':
        if cc == p:
            print('You lose :(')
        elif cc == s:
            print('You win :)')
        else:
            print('You draw :/')
        break
    elif yc == 'p':
        if cc == s:
            print('You lose :(')
        elif cc == r:
            print('You win :)')
        else:
            print('You draw :/')
        break
    elif yc == 's':
        if cc == 'r':
            print('You lose :(')
        elif cc == 'p':
            print('You win :)')
        else:
            print('You draw :/')
        break
    else:
        print('Invalid value, try again.')
        continue







