n = int(input())
arr = [0] + list(map(int, input().split()))

length = 21

dp = [[0] * length for _ in range(n)]
dp[1][arr[1]] = 1
for d in dp:
    print(d)

for i in range(2, n):
    print(i)
    for j in range(length):
        print(i, j)
        if j - arr[i] >= 0:
            dp[i][j] += dp[i - 1][j - arr[i]]
        if j + arr[i] < length:
            dp[i][j] += dp[i - 1][j + arr[i]]

for d in dp:
    print(d)
print(dp[-1][arr[-1]])
