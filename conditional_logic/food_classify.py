# NO TOUCHING ============================================
from random import choice
food = choice(['apple', 'grape', 'bacon', 'steak', 'worm', 'dirt'])
# NO TOUCHING =============================================

print(food)
# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

if (food == 'apple' or food == 'grape'):
    print('fruit')
elif (food == 'bacon' or food == 'steak'):
    print('meat')
else:
    print('yuck')
