salary = float(input('Enter a salary value: '))
new_salary = 0.0
if(salary>1250):
    new_salary = (salary * 0.10) + salary
else:
    new_salary = (salary * 0.15) + salary
print('The update salary: {}'.format(new_salary))