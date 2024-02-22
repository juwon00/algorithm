n = int(input())
a = list(map(int, input().split()))
s = int(input())

for i in range(n):

    if s <= 0:
        break

    # print(min(n, i + s + 1), "min")
    max_num = max(a[i: min(n, i + s + 1)])
    # print(max_num)
    idx = a.index(max_num)
    # print("idx", idx)

    for j in range(idx, i, -1):
        a[j], a[j-1] = a[j-1], a[j]

    # print(a)

    s -= (idx - i)

    # print("s", s)
    # print()


print(*a)
