import sys
from datetime import datetime
# генератор на range очень мало занимает в памяти, очень быстро создаётся, но он не собирается (не итерируется)
start = datetime.now()
print(f'Start working at {start} ')
r = range(100_000_000)

print(f'size of object {sys.getsizeof(r)}')
print(f'Working time {datetime.now() - start}')