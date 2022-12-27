# проверяем нахождение значения в генераторе

def func_gen(n):
    cnt = 0
    while cnt < n:
        yield cnt
        cnt += 1


d = func_gen(100_000)
print(99943 in d)
print(list(d))
print(99943 in d)  # второй раз он уже не найдет значение, потому что указатель переместился
