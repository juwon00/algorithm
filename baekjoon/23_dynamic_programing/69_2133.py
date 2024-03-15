n = int(input())
dp = [0] * 31
dp[2] = 3
print(dp)
for i in range(4, n + 1, 2):
    print(i, sum(dp[:i - 2]))
    dp[i] = dp[i - 2] * 3 + 2 * sum(dp[:i - 2]) + 2

    print(dp)
print(dp[n])
