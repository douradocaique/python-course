
# **LEARNING MANIPULATION TEXT IS VERY IMPORTANT IN PYTHON.**

### WHATS IS STRINGS?
example: 
`'Curso em Vídeo Python'`
    
In python, all strings they are between single quotes or double quotes
Is possible the use three quotes for long text

### THE STRING ATTRIBUTION
`phrase = 'Curso em Vídeo Python'`
The Python storing the variable in memory and broken in micro spaces each character - have a different address in memory
![alt text](9a-text-manipulation.png)

>[!NOTE]
> Those address start in 0



### THE MAIN OPERATIONS IS:
#### 🔪 STRING SLICING
example:

```
phrase[9]  #the return is character in position 9 of string
// V

phrase[9:13] #the return is characters are in position 9 to 12 - 13 characters no entry
// Víde

phrase[9:21] #the return is characters are in position 9 to 20
// Vídeo Python

phrase[9:21:2] #the return characters are in position 9 to 20, jumping two at a time
// VdoPto

phrase[:5] #the return characters are in position 0 to 4
// Curso

phrase[15:] #the return characters are in position 15 to end. This is best practice for getting the end
// Python

phrase[9::3] #the return characters are in position 9 to end, jumping three at a time
// VePh

```


#### 📉 ANALYSIS:
`len()`, `count()`, `find()`

example
```
len(phrase) #the fuction returns the number of characters contained in the string
// 21

phrase.count('o') #returns the number of times that character 'o' to appears. There is a difference between Upper and lower case
// 3

phrase.find('Curso') #fetches the parameter value and returns the position start the value found in string. There is a difference between Upper and lower case. Case not found, the returns -1
// 0

```

#### 🔄️ TRANSFORMATIONS:
`replace()`, `upper()`, `lower()`, `capitalize()`, `title()`, `strip()` and `join()`
>[!NOTE]
>All strings they are immutables

 ```
 phrase.replace('Python', 'Android') #change the value 'Python' to 'Android'
 // Curso em Vídeo Android

phrase.upper() #convert a string to uppercase
// CURSO EM VÍDEO PYTHON

phrase.lower() #convert a string to lowercase
// curso em vídeo python

phrase.capitalize() #convert the first letter of the string to uppercase
// Curso em vídeo python

phrase.title() #convert all first letters of the string to uppercase
// Curso Em Vídeo Python

prase.strip() #remove all whitespaces before and/or after the actual string. rstrip() or lstrip() - remove only whitespaces to right/left
// Curso Em Vídeo Python

 ```

 ### STRING DIVISION
```
 phrase.split() #splits the string according to space
 // ['Curso', 'em', 'Vídeo', 'Python']
```

### STRING JOIN
```
'-'.join(phrase) #joins the all elements, the separator is '-'. iclude whitespaces
// C-u-r-s-o- -e-m- -V-í-d-e-o- -P-y-t-h-o-n

```
