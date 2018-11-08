__author__ = 'stanislav-kuhtinski'

# Task1 - Sorting
list_to_sort = [4, 3, 8, 1, 0, 7, 5, 9]

sorted1 = sorted(list_to_sort)
sorted2 = sorted(list_to_sort, reverse=True)
print('Sorted list 1 = ', sorted1)
print('Sorted list 2 = ', sorted2)

list_to_sort.sort()  # if you do not need the original list
print('Sorted list 3 = ', list_to_sort)

# Task2 - tuple with float numbers, find max and min value
tuple_values = (0.23, 1.16, 0.001, 2.17, 0.02, -3.56, 12.22, 2.13, 3.43, 0.67,)
# print('Max value is ', max(tuple_values))
# print('Min value is ', min(tuple_values))
max_v = min_v = tuple_values[0]
for item in tuple_values:  # tuple is iterable
    if item > max_v:
        max_v = item
    elif item < min_v:
        min_v = item
print('Max valie is %s, Min value is %s' % (max_v, min_v))

# Task 3 - list to string
address = ['Earth', 'Estonia', 'Tallinn', 'Kivila4']
address_string = ''
# address_string = str(address[0] + ' -> ' + address[1] + ' -> ' + address[2])
for part in address:
    if not '':
        address_string += part
    if part != address[-1]:
        address_string += ' -> '
print("\nPosting address is ", address_string)

# Task 3 - separate string into list by symbol
path = '/bin:/usr/bin:/usr/local/bin'
path_parts = path.split(':')
print('List of path_parts', path_parts)
print('Full path is: ', path_parts[-1])

# Task 4 - all numbers in range(1-100) divided by 7
list_of_outputs = []  # empty list
for i in range(100):
    if i % 7 == 0:
        list_of_outputs.append(i)
print('\nValues in range 100 divided by 7: ', list_of_outputs)

# Task 5 - delete some value in list
some_data = ['to-delete', '1', 'to-delete', '2', '3', '4', 'to-delete', '5']
print('\nOriginal list: ', some_data)
# some_data = [data for data in some_data if data != 'to-delete']
while 'to-delete' in some_data:
    some_data.remove('to-delete')
print('Corrected list: ', some_data)
