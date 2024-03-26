# 다시 풀어볼 문제
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [[x for x in arr] for _ in range(2)]
print(dp)

for i in range(1, n):
    print(i)
    dp[0][i] = max(dp[0][i], dp[0][i - 1] + arr[i])
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + arr[i])
    print(dp)
print(max(max(dp[0]), max(dp[1])))
