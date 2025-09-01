h = float(input('Enter your height (m): '))
p = float(input('Enter your weight (kg): '))
print('CALCULATE YOUR IMC...')
imc = p/(h**2)

print('Your IMC: {:.2f}'.format(imc))
if(imc < 18.5):
    print('\033[1;;42m Underweight \033[m')
elif(imc >= 18.5 and imc <= 25):
    print('\033[1;;42m Ideal weight \033[m')
elif(imc> 25 and imc <= 30):
    print('\033[1;;43m Overweight \033[m')
elif(imc> 30 and imc <=40):
    print('\033[1;;45m Obesity \033[m')
else:
    print('\033[1;;41m Morbid obesity \033[m')
