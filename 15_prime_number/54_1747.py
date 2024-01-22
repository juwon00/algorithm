import math


def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def is_palindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    return False


n = int(input())

while True:
    if is_palindrome(n) and is_prime_number(n):
        print(n)
        break
    n += 1
