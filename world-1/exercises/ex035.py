a = float(input('Enter a line length (a): '))
b = float(input('Enter a line length (b): '))
c = float(input('Enter a line length (c): '))
a_b_c, a_c_b, b_c_a  = False, False, False

if((a+b)>c):
    a_b_c = True
if((a+c)>b):
    a_c_b = True
if((b+c)>a):
    b_c_a = True

if(a_b_c == a_c_b == b_c_a):
    print('The lines form a triangle')
else:
     print('The lines not form a triangle')
