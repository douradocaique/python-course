from math import hypot

opp_cath = float(input('Enter a value to opposite catheter: '))
adj_cath = float(input('Enter a value to adjacente catheter: '))
hypotenuse = hypot(opp_cath, adj_cath)

print('The hypotenuse is: {}'.format(hypotenuse))