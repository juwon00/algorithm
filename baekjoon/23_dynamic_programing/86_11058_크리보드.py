n = int(input())
dp = [0] * 101
for i in range(7):
    dp[i] = i
print(dp)

# v연산은 최대 3번까지 가능하다고 함, 즉 dp[i-6] * 5 는 필요 없었음
for i in range(7, 101):
    dp[i] = max(dp[i - 1] + 1, dp[i - 3] * 2, dp[i - 4] * 3, dp[i - 5] * 4, dp[i - 6] * 5)
print(dp)
print(dp[n])
