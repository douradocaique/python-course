number = int(input('Enter a number: '))
unit = number // 1 % 10
ten = number // 10 % 10
hundred = number // 100 % 10
thousand = number // 1000 % 10

print('''
    Unit: {}
    Ten: {}
    Hundred: {}
    Thousand: {}

'''.format(unit, ten, hundred, thousand))