# **CONDITIONALS IN PYTHON**

## WHAT IS CONDITIONALS? 
In Python language, the majority programs need conditions to work.
The conditions give us possibilities create a intelligent software.

## USE CONDITIONALS
```
n = int(input('Enter a value: '))
if(n>10):
    print('The value is greather than 10')
else:
    print('The value is less than 10')
```

Code based on above, the program he has two possibilities at execution, the block if or the block else

### Others examples
```
years_car = int(input('How many your car? '))
if(years_car < 3):
    print('Your car is new')
else:
    print('Your car is old')
```
```
name = str(input('Enter a first name: ')).strip()
verified_name = 'caique'
if(name.lower() == verified_name):
    print('Uau! The name is beautiful')
else:
    print('Arg! The name is bad')

```