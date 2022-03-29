# Problem 1
"""
def get_title(text):
    res = text.title()
    return res
"""

# Problem 2
"""
with open('new_file.txt', 'w') as file:
    file.write('The Zen of Python')
def read_file():
    with open('new_file.txt', 'r') as file:
        info = file.read()
        vrem = []
        for i in info.split():
            if i[0].lower() == 'c':
                vrem.append(i)
    return vrem
"""

# Problem 3
"""
'''выдает деньги с номиналом 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 3, 1'''
def bankomat(number):
    money = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 3, 1]
    give = []
    while number != 0:
        if number >= money[0]:
            give.append(money[0])
            number -= money[0]
        elif number >= money[1]:
            give.append(money[1])
            number -= money[1]
        elif number >= money[2]:
            give.append(money[2])
            number -= money[2]
        elif number >= money[3]:
            give.append(money[3])
            number -= money[3]
        elif number >= money[4]:
            give.append(money[4])
            number -= money[4]
        elif number >= money[5]:
            give.append(money[5])
            number -= money[5]
        elif number >= money[6]:
            give.append(money[6])
            number -= money[6]
        elif number >= money[7]:
            give.append(money[7])
            number -= money[7]
        elif number >= money[8]:
            give.append(money[8])
            number -= money[8]
        elif number >= money[9]:
            give.append(money[9])
            number -= money[9]
        elif number >= money[10]:
            give.append(money[10])
            number -= money[10]
        elif number >= money[11]:
            give.append(money[11])
            number -= money[11]
        else:
            give = []
    return give

print(bankomat(1456))
"""

# Problem 4
"""
def inner_func(number1, number2):
    res = number1 / number2
    return res   
def get_numbers(number1, number2):
    res = number1 * number2
    i = inner_func(7, 8)
    return res + i
"""

# Problem 5
"""
# 5
# Фильтрация с помощью filter(). Необходимо написать функцию, и передать ее filter(),
# чтобы получить список только тех слов из текста text (см. выше “The Zen of Python”), что содержат букву ‘p’.
# Подсказка: необходимо заменить \n на пробел.
# То есть, это нужно проделать еще до фильтрации.
# Функция, которая будет передана в filter() должна возвращать True, если в слове есть буква ‘p’.

text = '''
The Zen of Python, by Tim PetersBeautiful is better than ugly.Explicit is better than implicit.
Simple is better than complex.Complex is better than complicated.
Flat is better than nested.Sparse is better than dense.
Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.
Errors should never pass silently.Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one--and preferably only onUP,BROADCAST,RUNNING,MULTICASTe --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea --let's do more of those!
'''


def get_p(text):
    vrem = []
    for i in text.split():
        if 'p' in i.lower():
            vrem.append(i)

    def innerfunc(word):
        if 'p' in word:
            return True
        else:
            return False

    return filter(innerfunc, vrem)


adults = get_p(text)
for i in adults:
    print(i)
"""

# Problem 6
