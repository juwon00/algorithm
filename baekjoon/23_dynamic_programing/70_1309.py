n = int(input())
dp = [[0] * (n + 1) for _ in range(2)]
dp[0][1], dp[1][1] = 1, 2
for d in dp:
    print(d)

for i in range(2, n + 1):
    print(i)
    dp[0][i] = (dp[0][i - 1] + dp[1][i - 1]) % 9901
    dp[1][i] = (dp[0][i] + dp[0][i - 1]) % 9901

for d in dp:
    print(d)
result = dp[0][n] + dp[1][n]
print(result % 9901)
