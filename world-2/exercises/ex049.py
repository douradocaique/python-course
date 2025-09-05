i = int(input('Enter a value: '))


print('''
[1] - SUM (+)
[2] - SUBTRACTION (-)
[3] - MULTIPLICATION (*)
[4] - DIVISION (/)
''')

opt = int(input('Enter the operation: '))

if opt == 1:
    #SUM
    for n in range(1,10):
        print(f'{i} + {n} = {i+n}')

elif opt == 2:
    #SUBTRATION
    for n in range(1,10):
        print(f'{i} - {n} = {i-n}')
elif opt == 3:
    #MULTIPLICATION
    for n in range(1,10):
        print(f'{i} * {n} = {i*n}')
elif opt == 4:
    for n in range(1,10):
        print(f'{i} / {n} = {i/n}')




