name = str(input('Enter your name: ')).strip()
upper_name = name.upper()
lower_name = name.lower()
lenght_name = len(name) - name.count(' ')
split_name = name.split()

print('''
    Your name in uppercase: {}
    Your name in lowercase: {}
    Your name length: {}
    Your first name: {} and {} letters

'''.format(upper_name,lower_name,lenght_name, split_name[0], len(split_name[0])))