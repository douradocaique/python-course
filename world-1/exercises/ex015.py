days = int(input('How many days rented? '))
km = float(input('How many km traveled? '))
daily_car_rate = 60.00
km_rate = 0.15

total_price = (days * daily_car_rate) + (km*km_rate)
print('The total to be paid is: R${}'.format(total_price))


