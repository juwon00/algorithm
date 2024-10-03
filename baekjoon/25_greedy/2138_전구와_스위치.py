# 다시 풀어볼 문제

n = int(input())
bulb = list(map(int, input().strip()))
target = list(map(int, input().strip()))

print(bulb)
print(target)
print()


def push(A, B):
    A_copy = A[:]
    press = 0
    for i in range(1, n):
        print(i)
        print(A_copy)
        if A_copy[i - 1] == B[i - 1]:
            print()
            continue
        press += 1
        for j in range(i - 1, i + 2):
            print("j", j)
            if j < n:
                A_copy[j] = 1 - A_copy[j]
        print(A_copy)
        print()

    print("A_copy", A_copy)

    return press if A_copy == B else 1e9


tmp1 = push(bulb, target)
print(tmp1)
print("================")

bulb[0] = 1 - bulb[0]
bulb[1] = 1 - bulb[1]
tmp2 = push(bulb, target) + 1
print(tmp2)

result = min(tmp1, tmp2)
print(result if result != 1e9 else -1)
