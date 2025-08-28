name = str(input('Enter your name: '))
name = name.split()
first_name = name[0]
last_name = name[-1]
print('First Name: {}\nLast Name: {}'.format(first_name, last_name))