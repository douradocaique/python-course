meters=float(input('Enter a value in m(meters): '))
meters_centimeters = meters*60
meters_milimeters = meters * 1000
print('{:=^30}'.format(' CONVERSION '))
print('Value in cm: {}'.format(meters_centimeters))
print('Value in mm: {}'.format(meters_milimeters))