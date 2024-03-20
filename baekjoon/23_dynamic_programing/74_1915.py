n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input())))
for a in arr:
    print(a)

dp = [[0] * (m + 1) for _ in range(n + 1)]
for d in dp:
    print(d)

result = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        print(i, j)
        if arr[i - 1][j - 1] == 0:
            continue
        else:
            dp[i][j] = arr[i - 1][j - 1] + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
            result = max(result, dp[i][j])

for d in dp:
    print(d)

print(result * result)
