import string

tmp = string.digits + string.ascii_uppercase


# 다음에는 tmp말고 ['0123456789ABCDEF'] 같은것을 써서 풀어볼것
def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


def solution(n, t, m, p):
    print(n, t, m, p)
    answer = ''

    bases = '0'
    i = 1
    while True:
        if i > t * m:
            break
        bases += convert(i, n)
        i += 1
    print(bases, len(bases))

    for i in range(p - 1, t * m, m):
        print(i)
        answer += bases[i]

    return answer


n = 16
t = 16
m = 2
p = 1
answer = solution(n, t, m, p)
print("answer:", answer)
