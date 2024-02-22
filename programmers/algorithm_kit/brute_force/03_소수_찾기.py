from itertools import permutations


def is_prime(x):  # 소수 판별 함수
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0

    n = list(numbers)
    print(n)

    a = []
    for i in range(1, len(n) + 1):
        print(i)
        print(list(permutations(n, i)))
        a += list(permutations(n, i))
    print(a)

    b = []
    for i in a:
        print(int(''.join(i)))
        b.append(int(''.join(i)))
    b = list(set(b))
    print(b)

    for i in b:
        if i <= 1:
            continue
        elif is_prime(i):
            answer += 1

    return answer


numbers = "011"
solution(numbers)
