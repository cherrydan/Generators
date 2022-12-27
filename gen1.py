import sys
from datetime import datetime


# генератор на yeild мало занимает в памяти, быстро создаётся, но медленно собирается

def func_gen(n):
    cnt = 0
    while cnt < n:
        yield cnt
        cnt += 1


start = datetime.now()
print(f'Start working at {start} ')
d = func_gen(100_000_000)
try:
    while True:
        next(d)
except StopIteration:
    print('Ended')

print(f'size of object {sys.getsizeof(d)}')
print(f'Working time {datetime.now() - start}')
