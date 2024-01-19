import math


def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


m = int(input())
n = int(input())

result = []
for i in range(m, n + 1):
    print(i)
    if is_prime_number(i) and i > 1:
        result.append(i)

if len(result) > 0:
    print(sum(result))
    print(min(result))
else:
    print(-1)
