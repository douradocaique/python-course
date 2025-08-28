v = int(input('What is the speed car? '))
km_fine_price = 7.0
if(v> 80.0):
    print('You were fined in ${}'.format((v-80.0)*km_fine_price))
