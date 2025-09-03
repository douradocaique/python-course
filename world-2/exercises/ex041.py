from datetime import date
print('NATIONAL SWIMMING CONFEDERATION')
athlete_year = int(input('Enter the birth year of athlete: '))
year_now = date.today().year
age = year_now - athlete_year

if(age <= 9):
    print('YOUNG ATHLETE')
elif(age <= 14):
    print('CHILDREN ATHLETE')
elif(age <= 19):
    print('JUNIOR ATHLETE')
elif(age <= 25):
    print('SENIOR ATHLETE')
else:
    print('MASTER ATHLETE')