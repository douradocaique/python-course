from time import sleep
print('\033[1;;43m{:=^50}\033[m'.format(' WELCOME TO THE GOLD BANK '))
print('REAL ESTATE FINANCING')
property_value= float(input('Enter property value: '))
your_salary = float(input('Enter your salary amounbt: '))
years = float(input('Enter how many years you want to pay: '))

percent = 0.3
status = False
print('WAITING...')
sleep(3)

installment_value = property_value / (years*12)

if((your_salary*percent)>= installment_value):
    status = True
    if(status):
        print('FINANCING DETAILS')
        print('''
            STATUS: \033[1;;42m{}\033[m
            PROPERTY VALUE U$: {}
            YOUR SALARY U$: {}
            YEARS: {}
            INSTALLMENT NUMBERS: {}   
            INSTALLMENT VALUE: ${}
        '''.format('APPROVED', property_value, your_salary, years, (years*12),installment_value))

else:
    print('FINANCING DETAILS')
    print('''
        STATUS: \033[1;;41m{}\033[m
        PROPERTY VALUE U$: {}
        YOUR SALARY U$: {}
        YEARS: {}
        INSTALLMENT NUMBERS: {}
        INSTALLMENT VALUE: ${} 
        '''.format('REFUSED', property_value, your_salary, years, (years*12), installment_value))

