v = input('Enter a value: ')
print('''
    \033[1;;40mType: {}\033[m
    \033[1;;41mIs numeric?: {}\033[m
    \033[1;;42mIs alphabeth?: {}\033[m
    \033[1;;43mIs float?: {}\033[m
    \033[1;;44mIs alphanumeric?: {}\033[m
    \033[1;;45mIs capital: {}\033[m
    \033[1;;46mIs lowercase: {}\033[m
    \033[1;;47mContains spaces?: {}\033[m
    \033[1;;40mIs capitalized?: {}\033[m
    

'''.format(type(v), v.isnumeric(), v.isalpha(), v.isdecimal(),v.isalnum(), v.isupper(), v.islower(), v.isspace(), v.istitle()))