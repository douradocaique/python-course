from random import randint
from time import sleep
print('{:=^30}'.format('THE RANDOM GAME'))
n = int(input('Enter a number from 0 to 5: '))

print('Thinking of a number...')
sleep(3)
n_random = randint(0,5)
if(n == n_random):
    print('Uau! YOU WIN')
else:
    print('YOU LOSE!\nThe value is {}'.format(n_random))
print('{:=^30}'.format('THE END'))
