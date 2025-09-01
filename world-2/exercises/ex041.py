from datetime import date
print('NATIONAL SWIMMING CONFEDERATION')
athlete_year = int(input('Enter the birth year of athlete: '))
year_now = date.today().year
age = year_now - athlete_year

if(age <= 9):
    print('YOUNG ATHLETE')
elif(age >= 9 and age <= 14):
    print('CHILDREN ATHLETE')
elif(age > 14 and age <= 19):
    print('JUNIOR ATHLETE')
elif(age > 19 and age <= 20):
    print('SENIOR ATHLETE')
else:
    print('MASTER ATHLETE')