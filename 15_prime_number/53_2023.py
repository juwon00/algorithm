# 백트래킹, 다시 생각해볼 문제

import math

n = int(input())


def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if int(x) % i == 0:
            return False
    return True


def dfs(num):
    if len(str(num)) == n:
        print("num", num)
    else:
        for i in range(1, 10, 2):
            tmp = num * 10 + i
            print(tmp)
            if is_prime_number(tmp):
                dfs(tmp)


dfs(2)
dfs(3)
dfs(5)
dfs(7)
