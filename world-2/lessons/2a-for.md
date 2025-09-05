# **FOR IN PYTHON**
The idea of ​​for is to repeat a block of code for each item.
Imagine a deck of cards, where the goal would be to flip over all the cards, one by one. This would be a repetitive action. For would do just that. It would pick a card, perform the action, then the next, and the next, until there were no more cards in the deck.

### How does for work?
The basic syntax is:
```
for item in sequence:
    # do something with the item
```

```for```: The word-key what starts loop
```item```: It is a temporary variable that stores the value of each item in the sequence at each repetition.
```in```: The keyword that indicates that the temporary variable will loop through the sequence.
```sequence```: It can be a list, a tuple, a string, or any object that contains items.

### Practical Examples
Let's see the for loop in action with some types of sequences:

1. With a list (the most common use)
```
fruits = ['apple','banana','grape','orange']
for fruit in fruits:
    print(f'I like fruit {fruit}.')
```

2. With a string
A string is a sequence of characters. The for loop can iterate over each letter.
```
word = 'Python'
for w in word:
    print(w)
```
3. With the range() function
The range() function is very useful for repeating an action a specific number of times. It generates a sequence of numbers.

```
for n in range(5):
    print(f'its value: {n}')
```
range() accepts up to three arguments:
start: The number where the sequence begins.
stop: The number where the sequence stops (the sequence does not include this number).
step: The value that the sequence "jumps" at each step (if negative, the count is backward).

