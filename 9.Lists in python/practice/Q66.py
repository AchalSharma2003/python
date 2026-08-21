"""
Using list comprehension, create a list of squares of all odd numbers 
from 1 to 20.
"""

new_lst = [i * i for i in range(1, 21) if i%2 != 0]
print(new_lst)