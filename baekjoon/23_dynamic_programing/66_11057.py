n = int(input())

dp = [[0] * 11 for _ in range(n + 1)]

for d in dp:
    print(d)

for i in range(1, n + 1):
    print(i)
    for j in range(1, 11):
        print(i, j)
        if i == 1:
            dp[i][j] = 1
        elif j == 1:
            dp[i][j] = sum(dp[i - 1])
        else:
            dp[i][j] = dp[i][j - 1] - dp[i - 1][j - 1]

for d in dp:
    print(d)
print(sum(dp[n]) % 10007)
