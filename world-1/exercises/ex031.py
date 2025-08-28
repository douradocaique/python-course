distance = float(input('Enter the distance traveled: '))
if(distance <= 200):
    print('The value is ${}'.format(distance*0.50))
else:
    print('The value is ${}'.format(distance*0.45))