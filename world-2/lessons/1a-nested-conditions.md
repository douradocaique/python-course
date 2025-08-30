# **NESTED CONDITIONS**

These refer to conditional structures (if, elif, else) that are placed within other conditional structures. This allows for the creation of more complex decisions, where different conditions can be evaluated sequentially, based on the outcome of previous conditions.

### How they work:
A nested condition is basically an if, elif, or else statement contained within the code block of another if, elif, or else statement. This means that, depending on the outcome of an outer condition, another condition can be evaluated, and so on, creating multiple levels of decision-making.

Example:
```
age = 18
has_card = true
if(age >= 18):
    if(has_card):
        print('You can buy the product.')
    else:
    print('You need a card to buy.')
else:
    print('You are under 18 and cannot buy.')
```