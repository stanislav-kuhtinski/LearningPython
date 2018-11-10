__author__ = 'stanislav-kuhtinski'
import traceback


# Task 6 - string to caps
def transform_uppercase(some_string, flag=True):
    try:
        if flag == True:
            return str(some_string).upper()
        else:
            return str(some_string).lower()
    except Exception as error:
        message = traceback.format_exc()
        print('Exception! Error code is ', error, message)


print(transform_uppercase('Stanislav', False))


# Task 5 - max and min
def max_min(*numbers): #unlimited number of positional arguments
    try:
        max_value = max(numbers)
        min_value = min(numbers)
        return (max_value, min_value)
    except Exception as error:
        message = traceback.format_exc()
        print('Exception! Error code is ', error, message)


returned_tuple = max_min(0.23, 1.16, 0.001, 2.17, 0.02, -3.56, 12.22, 2.13, 3.43, 0.67, )
print('Max value is {}, min value is {}'.format(returned_tuple[0], returned_tuple[1]))


# Task 4 - func sort a list with int values
def sort_ints_list(ints_list):
    try:
        ints_list.sort()
        print('Your list has been sorted ', ints_list)
    except ValueError:
        print('Error value, all values should be numbers')
    except TypeError:
        print('Error type, all values should be numbers')
    except Exception as error:
        message = traceback.format_exc()
        print('Exception! Error code is ', error, message)


list_to_sort = [4, 3, 8, 6, 0, 7, 5, 9]
sort_ints_list(list_to_sort)

# Task3 - take an object from the list by index
kitchen_items = [
    "Rice", "Chickpeas", "Pulses", "bread", "meat",
    "Milk", "Bacon", "Eggs", "Rice Cooker", "Sauce",
    "Chicken Pie", "Apple Pie", "Pudding"
]
try:
    user_input = int(input('Please enter the index number: '))
    print('Here is the object from the list - ', kitchen_items[user_input])
except ValueError:
    print('Error, index should be a number')
except IndexError:
    print('Error, there is no such index')
except Exception as error:
    message = traceback.format_exc()
    print('Exception! Error code is ', error, message)

# Task2 - if value is even - throw a ValueError exception, if it is less than 0 - TypeError, if it is more than 10 - IndexError.
# user_input = int(input('Please enter a number: '))
try:
    if user_input % 2 == 0:
        raise ValueError()
    if user_input < 0:
        raise TypeError()
    if user_input > 10:
        raise IndexError()
    else:
        raise Exception
except ValueError:
    print('The entered value is even')
except TypeError:
    print('The entered value is less then 0')
except IndexError:
    print('The entered value is more then 10')
except Exception as unknown:
    print("I don't know what's going on!")
    print(unknown)


# Task1 - Function that multiplies all the values
def multiple_all(*numbers):
    composition = 1
    for item in numbers:
        composition *= item
        print(composition)


multiple_all(-0.25, 12, 3, -0.01)
