import numpy as np
import datetime


# add two number
def add(a, b):
    return a + b
# return a string of the datetime
def get_datetime():
    return str(datetime.datetime.now())


# get a random string with a-z and 0-9
def get_random_string():
    return ''.join(np.random.choice(list('abcdefghijklmnopqrstuvwxyz0123456789'), 10))

# get a random string with both letters and numbers with the length of 20
def get_random_string_20():
    return ''.join(np.random.choice(list('abcdefghijklmnopqrstuvwxyz0123456789'), 20))

# get a random string with both letters and numbers with the length of 20 without reptation
def get_random_string_20_without_reptation():
    return ''.join(np.random.choice(list('abcdefghijklmnopqrstuvwxyz0123456789'), 20, replace=False))

a = get_random_string_20()
print(a)
b = get_random_string_20_without_reptation()
print(b)
