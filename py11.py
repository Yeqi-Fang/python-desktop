import time

def timer(func):
    def inner(*args, **kwargs):
        t1 = time.perf_counter()
        func(*args, **kwargs)
        t2 = time.perf_counter()
        print(f'Time is {t2-t1}')
    return inner
@timer
def test1():
    a = 0
    for i in range(int(1e7)):
        a += 1
# print(1)

test1()





