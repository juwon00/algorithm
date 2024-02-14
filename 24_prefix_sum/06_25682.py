# 2차원 누적합 - 나중에 다시 한번 더 볼만한 문제
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

data = [input().rstrip() for _ in range(n)]

b_prefix = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
w_prefix = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

print(data)
print(b_prefix)
print(w_prefix)

for i in range(n):
    for j in range(m):
        print(i, j, ((i + j) % 2))
        if (i + j) % 2:
            if data[i][j] == 'B':
                b_prefix[i][j] = 1 + b_prefix[i - 1][j] + b_prefix[i][j - 1] - b_prefix[i - 1][j - 1]
                w_prefix[i][j] = 0 + w_prefix[i - 1][j] + w_prefix[i][j - 1] - w_prefix[i - 1][j - 1]
            else:
                b_prefix[i][j] = 0 + b_prefix[i - 1][j] + b_prefix[i][j - 1] - b_prefix[i - 1][j - 1]
                w_prefix[i][j] = 1 + w_prefix[i - 1][j] + w_prefix[i][j - 1] - w_prefix[i - 1][j - 1]
        else:
            if data[i][j] == 'B':
                b_prefix[i][j] = 0 + b_prefix[i - 1][j] + b_prefix[i][j - 1] - b_prefix[i - 1][j - 1]
                w_prefix[i][j] = 1 + w_prefix[i - 1][j] + w_prefix[i][j - 1] - w_prefix[i - 1][j - 1]
            else:
                b_prefix[i][j] = 1 + b_prefix[i - 1][j] + b_prefix[i][j - 1] - b_prefix[i - 1][j - 1]
                w_prefix[i][j] = 0 + w_prefix[i - 1][j] + w_prefix[i][j - 1] - w_prefix[i - 1][j - 1]

for b in b_prefix:
    print(b)
print()
for w in w_prefix:
    print(w)

result = 4000000

for i in range(n - k + 1):
    for j in range(m - k + 1):
        print(i, j)
        b_sub_sum = b_prefix[i + k - 1][j + k - 1] - b_prefix[i - 1][j + k - 1] - b_prefix[i + k - 1][j - 1] + \
                    b_prefix[i - 1][j - 1]
        w_sub_sum = w_prefix[i + k - 1][j + k - 1] - w_prefix[i - 1][j + k - 1] - w_prefix[i + k - 1][j - 1] + \
                    w_prefix[i - 1][j - 1]
        result = min(result, b_sub_sum, w_sub_sum)

print(result)
