# Problem 1
"""
def my_reversed(iteral):
    res = []
    for i in iteral:
        res.insert(0, i)
    return res
"""

# Problem 2
"""
'''1,1,2,3,5,8,13,21,34'''
def fibanachi():
    count1 = 1
    count2 = 1
    fib = [count1, count2]
    for i in range(10):
        fib.append(fib[i]+fib[i+1])
    return fib
"""

# Problem 3
"""
def my_sum():
    return 5 + 9
def my_kemit():
    return 9 - 3
def vyzov():
    my_sum()
    my_kemit()
"""

# Problem 4
"""
name_file = input('Name file: ')
def create_file():
    with open(f'{name_file}.txt', 'w') as f:
        pass
func = create_file
func()
"""

# Problem 5
"""
from random import choice
def gen_number():
    a = list(set('145790'))
    r = ''
    for i in range(6):
        b = choice(a)
        r += b
    res = '0444' + r
    return res
"""

