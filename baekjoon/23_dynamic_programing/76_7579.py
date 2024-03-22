import sys

input = sys.stdin.readline

n, m = map(int, input().split())
A = [0] + list(map(int, input().split()))
C = [0] + list(map(int, input().split()))
dp = [[0] * (sum(C) + 1) for _ in range(n + 1)]

for d in dp:
    print(d)

for i in range(1, n + 1):
    print(i)
    for j in range(sum(C) + 1):
        print(i, j)
        if j < C[i]:
            print("pass")
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - C[i]] + A[i])

for d in dp:
    print(d)

for k in range(sum(C) + 1):
    if dp[n][k] >= m:
        print(k)
        break


