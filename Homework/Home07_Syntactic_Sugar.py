__author__ = 'stanislav-kuhtinski'

# lambda functions, map, filter, reduce
from functools import reduce

# Find Remainder Value of Division by 5
# var = map (func, list}
n1 = [1, 4, 5, 30, 99]
devided_by = 5
print('Inisiated list items ', n1, ' and the result ', list(map(lambda x: x % devided_by, n1)))

n2 = [3, 4, 90, -2]
print('Inisiated list items ', n2, ' and the result ', list(map(str, n2)))

# filter = filter(condition, list)
n3 = ['some', 1, 'v', 40, '3a', str]
print('Inisiated list items ', n3, ' and the result ', list(filter(lambda x: not isinstance(x, str), n3)))

# reduce = reduce(func, list}
n4 = ['some', 'other', 'value', 'given']
print('Inisiated list items ', n4, ' and the result ', reduce(lambda a, b: a + b, list(len(x) for x in n4)))
