__author__ = 'stanislav-kuhtinski'

from datetime import datetime


# --------------------------------------------------

def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            print('Exception \'{}\' occured while running \'{}\''.format(err, func.__name__))

    return wrapper


@exception_handler
def zero_divide(num):
    return 1 / num


@exception_handler
def add_two_numbers(x, y):
    sum = x + y
    print(sum)
    return sum


# --------------------------------------------------
# Task4. Logging decorator
def log_activity(func):
    print('Decorator has been called for function {}.'.format(func.__name__))

    def wrapper(*args, **kwargs):
        print('The initial function {} will execute now.'.format(func.__name__))
        func(*args, **kwargs)
        print('The initial function {} was executed.'.format(func.__name__))

    return wrapper


@log_activity
def time_to_sleep(seconds):
    import time
    time.sleep(seconds)


# --------------------------------------------------
# Task3. Count the function execution times
def count_executions(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        # print('result of func() ', func(*args, **kwargs))
        return func

    wrapper.calls = 0
    return wrapper


class MyList(list):
    @count_executions
    def sum_two_numbers(self, a, b):
        return (self, a + b)


pairs = MyList([1, 2, 3, 4, 5])
for i in range(len(pairs) - 1):
    pairs.sum_two_numbers(pairs[i], pairs[i + 1])
print('Fuction has been executed {} times'.format(pairs.sum_two_numbers.calls))


# --------------------------------------------------
# Task2. Measures the speed of functions performance
def measure_time(slow_funk):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        try:
            slow_funk(*args, **kwargs)
        except Exception as e:
            print('Type Error', e)
        print(slow_funk.__name__, ' executed in ', datetime.now() - start_time)

    return wrapper


@measure_time  # decorate for speed measurment
def slow_function(n=100000):
    total = 0
    for i in range(n):
        total += i
    return total


# --------------------------------------------------
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
    say_hello()
    slow_function()
    time_to_sleep(4)
    zero_divide()
    add_two_numbers(1, 'a')
