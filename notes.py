import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 1000)
y = np.sin(x)

plt.plot(x, y)
plt.show()

# Creating Decorator Class
class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('Call Method executed before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)

@decorator_class
def display_info(name, age):
    print('Display function executed with arguments ({}, {})'.format(name, age))
display_info("Megan", 21)

# Creating Decorator Function
def decorator_function(original):
    def wrapper_function(*args, **kwargs):
        print('Wrapper executed this before {}'.format(original.__name__))
        return original(*args, **kwargs)
    return wrapper_function

# @decorator_function
# def display_info_again(name, age):
#     print('Display function executed with arguments ({}, {})'.format(name, age))

# display_info_again("Sally", 41)

from functools import wraps

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    return wrapper

def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        t2 = time.time()-t1
        print('{} ran in {} sec'.format(orig_func.__name__, t2))
        return(orig_func(*args, **kwargs))
    return wrapper


import time
@my_logger
@my_timer
def display_info_again(name, age):
    time.sleep(1)
    print('The function executed with arguments ({}, {})'.format(name, age))

display_info_again("Max", 33)

def bg(task_id):
    lastdigit = task_id%10
    return('static/img/{}.png'.format(lastdigit))

bg(14)