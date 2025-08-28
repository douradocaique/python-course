wallet = float(input('How much do you have in your wallet? '))
dolar = 5.43
real_dolar = wallet/dolar
print('You have R${:.2f} and you can buy US${:.2f}'.format(wallet, real_dolar))