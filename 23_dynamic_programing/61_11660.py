import sys
input = sys.stdin.readline

n, m = map(int, input().split())

li = [[0] * (n + 1)]

for i in range(n):
    li.append([0])
    li[i + 1].extend(list(map(int, input().split())))

# for a in range(n + 1):
#     print(li[a])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        li[i][j] = li[i][j] + li[i - 1][j] + li[i][j - 1] - li[i - 1][j - 1]

# for a in range(n + 1):
#     print(li[a])

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    # print(x1, y1, x2, y2)
    # print()
    # print(x2, y2)
    # print(x2, y1-1)
    # print(x1-1, y2)
    # print(x1-1, y1-1)
    count = li[x2][y2] - li[x2][y1-1] - li[x1-1][y2] + li[x1-1][y1-1]
    print(count)
