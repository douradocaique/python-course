n1 = float(input('Enter a value for note 1: '))
n2 = float(input('Enter a value for note 2: '))
media = (n1 + n2)/2
if(media < 5):
    print('\033[1;;41m Failed \033[m')
elif(media >= 5 and media <= 6.9):
    print('\033[1;;43m Recovey \033[m')
else:
    print('\033[1;;42m Approved \033[m')