__author__ = 'stanislav-kuhtinski'

from datetime import datetime


# Task2. Measures the speed of functions performance
def measure_time(slow_funk):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        try:
            slow_funk(*args, **kwargs)
        except TypeError as e:
            print('Type Error', e)
        print(datetime.now() - start_time)
    return wrapper


@measure_time  # decorate for speed measurment
def slow_function(n=10000):
    total = 0
    for i in range(n):
        total += i
        print('{} total {}'.format(i, total))
    return total


# Task1. Cancels execution of any function
def cansel_function(func):
    def inner(*args, **kwargs):
        print(func.__name__, 'function is canceled')
        # func(*args, **kwargs)

    return inner


@cansel_function  # decorating say_hello for cancelation
def say_hello(name="everybody"):
    print("Hello " + name + "!")


if __name__ == '__main__':
    # Basic functions:
    # say_hello()
    slow_function()
