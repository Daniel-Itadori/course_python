print('Welcome to the username generator, this program creates a username with the exponetial distribution'
      ' (pdf and CDF), the number evaluated in the pdf and CDF will be in your username!')
fav_num = int(input('What is your favorite number between 0 and infinity?: '))
fav_lam = float(input('What is your favorite lambda?: '))
sign = input('What is your zodiac sing?: ')
pdf = fav_lam*pow(2.7182, -fav_lam*fav_num)
CDF = 1-pow(2.7182, -fav_lam*fav_num)
print(f'Your username is: {CDF}{sign}{pdf}')