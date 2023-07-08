import numpy as np
import time

step = int(1e7)
# start = time.perf_counter()
# a = np.ones(step)
# for i in range(step):
#     a[i] = i
# end = time.perf_counter()

# print(end - start)

start = time.perf_counter()
lst = []
for i in range(step):
    lst.append(i)

end = time.perf_counter()

print(end - start)