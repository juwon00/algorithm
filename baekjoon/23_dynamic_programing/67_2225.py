n, k = map(int, input().split())

dp = [1] * (n + 1)
print(dp)

for i in range(2, k + 1):
    for j in range(1, n + 1):
        print(i, j)
        if j == 1:
            dp[j] = i
        else:
            dp[j] += dp[j - 1]
print(dp)
print(dp[n] % 1000000000)
