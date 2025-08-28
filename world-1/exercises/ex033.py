n1 = float(input('Enter a first number: '))
n2 = float(input('Enter a secound number: '))
n3 = float(input('Enter a third number : '))
bigger = n1
if(n2> bigger):
    bigger = n2
if(n3>bigger):
    bigger = n3

lowlest = n1
if(n2<lowlest):
    lowlest = n2
if(n3<lowlest):
    lowlest = n3

print('The bigger number is {}\nThe lowlest number is {}'.format(bigger, lowlest))