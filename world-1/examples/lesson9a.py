phrase = 'Curso em Vídeo Python'

#STRING SLICING
print(phrase[9])
print(phrase[9:13])
print(phrase[9:21])
print(phrase[9:21:2])
print(phrase[:5])
print(phrase[:15])
print(phrase[9::3])

#ANALYSIS
print(len(phrase))
print(phrase.count('o'))
print(phrase.find('Curso'))


#TRANSFORMATIONS
print(phrase.replace('Python', 'Android'))
print(phrase.upper())
print(phrase.lower())
print(phrase.capitalize())
print(phrase.title())
phrase = '    Curso em Vídeo Python    '
print(phrase.strip())

#STRING DIVISION
phrase = 'Curso em Vídeo Python'
print(phrase.split())
print('-'.join(phrase))