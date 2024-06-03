"""
Your job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.
Small pizza (S): $15
Medium pizza (M): $20
Large pizza (L): $25
Add pepperoni for small pizza (Y or N): +$2
Add pepperoni for medium or large pizza (Y or N): +$3
Add extra cheese for any size pizza (Y or N): +$1
"""
bill = 0
size = input('What is the size?: small(S), medium(M), large(L).')

if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25
else:
    print('Value no recognize')


pepperoni = bool(int(input('Do you want pepperoni extra?: yes (1), no(0)')))
if pepperoni:
    bill += 3
    if size == 'S':
        bill -= 1

cheese = bool(int(input('Do you want cheese extra?: yes (1), no(0)')))
if cheese:
    bill += 1

print(bill)