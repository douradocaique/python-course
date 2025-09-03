from random import randint
print('Rochambeau')
print('''
Choose one of the values ​​below:
[0] - Rock
[1] - Paper 
[2] - Scissors
''')

player = int(input('Your option: '))
jokenpo = ['Rock', 'Paper', 'Scissors']
player_opt = jokenpo[player]
r = randint(0,2)
pc_opt = jokenpo[r]

if player_opt == pc_opt:
    print('\033[1;;43m Tie! \033[m')
elif player_opt != pc_opt:
    if player_opt == 'Rock' and pc_opt == 'Scissors':
        print('\033[1;;42m You Win! \033[m')
    elif player_opt == 'Paper' and pc_opt == 'Rock':
        print('\033[1;;42m You Win! \033[m')

    elif player_opt == 'Scissors' and pc_opt == 'Paper':
        print('\033[1;;42m You Win! \033[m')
    else:
        print('\033[1;;41m You Lose! \033[m')



print('You choose: {}\nPc choose: {}'.format(player_opt, pc_opt))


