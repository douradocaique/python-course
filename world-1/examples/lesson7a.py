# THE PRECEDENCE ORDER IS IMPORTANT
print(5+3*2)
print(3*5+4**2)
print(3*(5+4)**2)

# SUM A VALUES A LEFT AND COMPARE TO VALUE A RIGHT 
print(5+2==7) 

# USING THE POW() FUNCTION
print(pow(4,3))

# CALCULATE SQUARE ROOT
print(25**(1/2))

# CONCATENATE WORLDS
print('hello'+'hell')

# MULTIPLY WORLDS                                                                                                                                                                                                                                            
print('hello'*5)
print('='*20)

# FORMATED PRINT
name= 'Caique Dourado'
print('Welcome to sir/madam, {}!'.format(name))

# FILL IN 20 BLANK SPACES
print('Welcome to sir/madam, {:20}!'.format(name)) 

# FILL IN 20 BLANK SPACES AND ALIGN A RIGHT
print('Welcome to sir/madam {:>20}!'.format(name))

# FILL IN 20 BLANK SPACES AND ALIGN A LEFT
print('Welcome to sir/madam, {:<20}!'.format(name))

# FILL IN 20 BLANK SPACES AND CENTRALIZE THE VALUE VAR
print('Welcome to sir/madam, {:^20}!'.format(name))

# FILL IN 20 BLANK SPACES, CENTRALIZE VALUE VAR AND REPLACE BLANKS WITH '='
print('Welcome to sir/madam, {:=^20}!'.format(name))

# SUM INSIDE THE format()
print('The value of sum is {}'.format(5+5))

# REDUCE DECIMALS HOUSES
print('The value of pi is {:.3f}'.format(3,14159265))

# NOT BREAK THE LINE DISPLAY USING THE .format(), end=' '
print('Its first line of my program'.format(),end=' ')
print('Its second line of my program')

# BREAK THE LINE DISPLAY USING \n
print('Hello\nWorld')