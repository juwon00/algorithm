# 에라토스테니스의 체

import math

m, n = map(int, input().split())

array = [True for i in range(n + 1)]
print(array)
print(int(math.sqrt(n)) + 1)

for i in range(2, int(math.sqrt(n)) + 1):
    print("i", i)
    if array[i]:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

for i in range(m, n + 1):
    if array[i] and i > 1:
        print(i)
