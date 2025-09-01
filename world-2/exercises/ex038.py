print('{:*^20}'.format('THE GREATER VALUE IS...'))
n1 = int(input('Enter a value for n1: '))
n2 = int(input('Enter a value for n2: '))

if n1>n2:
    print('The first value ({}) is greater than the second value ({})'.format(n1, n2))
elif n2> n1:
    print('The second value ({}) is greater than the first value ({})'.format(n2, n1))
else:
    print('The values ​​are the same')
