salary = float(input('Enter the current salary R$: '))
growth = 0.15
new_salary = salary+(salary*growth) #or new_salary=salary+(salary*15/100)
print('New salário com reajuste de 15%: R${}'.format(new_salary))