from random import shuffle

s1 = input('Enter the name of the first student: ')
s2 = input('Enter the name of the secound student: ')
s3 = input('Enter the name of the third student: ')
s4 = input('Enter the name of the fourth studente:')

student_list = [s1, s2, s3, s4]
presentation_ordem =  shuffle(student_list)
print('The presentation ordem is: {}'.format(presentation_ordem))
