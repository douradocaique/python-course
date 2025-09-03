from datetime import date
print('THE MILITARY SERVICE OF BRAZIL')
birth_year = int(input('Enter your birth year: '))
year_now = date.today().year
age = year_now - birth_year


if age == 18:
    print('Congratulations, you are at the ideal age to enlist.')
elif age > 18:
    print('You have exceeded your enlistment time in {} years, go to one of our posts'.format(age-18))
elif age < 18:
    print('There are still {} year(s) to go'.format(18-age))