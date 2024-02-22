import math
import sys

input = sys.stdin.readline

while True:
    n = int(input())

    if n == 0:
        break

    array = [True for _ in range(2 * n + 1)]
    for i in range(2, int(math.sqrt(2 * n)) + 1):
        if array[i]:
            # print("i", i)
            j = 2
            while i * j <= 2 * n:
                # print(i * j)
                array[i * j] = False
                j += 1
    # print(array)
    result = 0
    for j in range(n + 1, 2 * n + 1):
        if array[j]:
            result += 1
    print(result)
