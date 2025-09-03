price = float(input('Enter a value for the product: '))
cash = 0.10
debit_card = 0.05
credit_card_3x = 0.2
new_price = 0.0
print('''
    Payments Methods
    [1] Cash
    [2] Debit Card
    [3] Credit Card 2x
    [4] Credit Card 3x
''')
opt = int(input('Choose the available payment method: '))
if opt == 1:
    new_price = price - (price*cash)
elif opt == 2:
    new_price = price - (price*debit_card)
elif opt == 3:
    new_price = price
elif opt == 4:
    new_price = price + (price*credit_card_3x)
else:
    print('Invalid option!')

print('The new value of the product: U${}'.format(new_price))

