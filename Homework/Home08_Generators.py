__author__ = 'stanislav-kuhtinski'

import random


# 4. zip generator
def my_zip(list_a, list_b):
    len_a = len(list_a)
    for x in range(0, len_a):
        yield [list_a[x], list_b[x]]


# 3. map generator
# var = map (func, list}
def double_score(x):
    return (x * x)


def my_map(func, my_list):
    for i in my_list:
        yield func(i)


# 2. range generator
def my_range(start, stop, step=1):
    i = start
    while i <= stop:
        yield i
        i += step


# 1. random generator
def give_random_number(end):
    yield (random.randint(0, end))


print('My Random number is', next(give_random_number(100)))
print('My Range is', list(my_range(1, 15)))
print('My Map is', list(my_map(double_score, [1, 2, 3, 4, 5])))
print('My Zip is', list(my_zip([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e'])))