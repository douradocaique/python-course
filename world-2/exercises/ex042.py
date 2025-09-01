r1 = int(input('Enter a value for line 1: '))
r2 = int(input('Enter a value for line 2: '))
r3 = int(input('Enter a value for line 3: '))
is_triangle = False
if((r1+r2)> r3 and (r1+r3)> r2 and (r2+r3)> r1):
    is_triangle = True
if(is_triangle):
    if(r1==r2 and r1 == r3):
        print('The triangle is equilateral')

    elif(r1 == r2 or r1 == r3 or r2 == r3 ):
        print('The triangle is isosceles')
    else:
        print('The triangle is scalene')
else:
    print('Lines r1, r2 and r3 do not form a triangle')
