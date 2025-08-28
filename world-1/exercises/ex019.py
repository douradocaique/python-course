from random import choice
s1 = input('Enter the name of the first student: ')
s2 = input('Enter the name of the secound student: ')
s3 = input('Enter the name of the third student: ')
s4 = input('Enter the name of the fourth studente:')
student_list = [s1, s2, s3, s4]
select_student = choice(student_list)

print('The selected student: {}'.format(select_student))
