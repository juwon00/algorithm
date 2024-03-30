# 50_9095 문제에서 심화된 문제, 다시 풀어볼 문제

dp = [1] * 100001

for i in range(2, 10001):
    dp[i] += dp[i - 2]

for j in range(3, 10001):
    dp[j] += dp[j - 3]

n = int(input())
for _ in range(n):
    print(dp[int(input())])
