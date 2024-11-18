n = int(input())
k = int(input())
dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[1][2] = 2
dp[1][3] = 3
for i in range(k + 1):
    for j in range(4, n + 1):
        print(i, j)
        if i == 1:
            dp[i][j] = j
            continue
        dp[i][j] = dp[i - 1][j - 2] + dp[i][j - 1]
        for d in dp:
            print(d)
        print()

print(dp[k][n] % (int(1e9) + 3))
