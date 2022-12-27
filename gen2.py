import sys
from datetime import datetime


# генератор на листе занимает больше всего памяти, и довольно медленно собирается

def func(n):
    res = []
    cnt = 0
    while cnt < n:
        res.append(cnt)
        cnt += 1
    return res


start = datetime.now()
print(f'Start working at {start} ')

l = func(100_000_000)
print(f'size of object {sys.getsizeof(l)}')
print(f'Working time {datetime.now() - start}')
