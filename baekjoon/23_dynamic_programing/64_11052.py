import sys

input = sys.stdin.readline

n = int(input())
dp = [0]
dp.extend(list(map(int, input().split())))
print(dp)

for i in range(1, n + 1):
    print("--- i", i, i // 2)
    for j in range(i // 2 + 1):
        print(i, j, i - j)
        dp[i] = max(dp[i], dp[i - j] + dp[j])

print(dp)
print(dp[n])
