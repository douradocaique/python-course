print('{:=^100}'.format(' DECIMAL BASE CONVERTER FOR: BINARY, OCTAL AND HEXADECIMAL '))
n = int(input('Enter a value: '))
print('AVAILABLE OPTIONS')
print('''
    [1] - Binary
    [2] - Octal
    [3] - Hexadecimal
''')

opt = int(input('You want to convert to: '))
nb = n
binary = ''
rest = 0
no = n
octal = ''
nh = n
hexa = ''

if(opt == 1):
    ##BINARY CONVERSION
    if nb == 0:
        binary = '0'
    while nb> 0:
        rest = nb % 2
        binary = str(rest) + binary
        nb= nb // 2
    print('The {} in Binary: {}'.format(n, binary))

elif (opt == 2):
    ##OCTAL CONVERSION
    if no ==0:
        octal = '0'
    while no > 0:
        rest = no % 8
        octal = str(rest) + octal
        no = no // 8 
    print('The {} in Octal: {}'.format(n, octal))

elif(opt == 3):
    ##CONVERT IN HEXADECIMAL
    if nh == 0:
        hexa = '0'
    while nh > 0:
        rest = nh%16
        if rest == 10:
            rest = 'A'
        if rest == 11:
            rest = 'B'
        if rest == 12:
            rest = 'C'
        if rest == 13:
            rest ='D'
        if rest == 14:
            rest = 'E'
        if rest == 15:
            rest = 'F'
        hexa = str(rest) + hexa
        
        nh = nh // 16
    print('The {} in Hexadecimal: {}'.format(n, hexa))
else:
    print('ALERT: You must choose one of the available options !!!')







