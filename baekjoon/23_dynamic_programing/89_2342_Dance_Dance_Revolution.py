# 다시 풀어볼 문제

import sys

input = sys.stdin.readline


def dist(now, move):
    if now == 0:
        return 2
    elif now == move:
        return 1
    elif abs(now - move) == 1 or abs(now - move) == 3:
        return 3
    elif abs(now - move) == 2:
        return 4


num = list(map(int, input().split()))
dp = [[[4 * len(num) for _ in range(5)] for _ in range(5)] for _ in range(len(num))]
dp[0][0][0] = 0
for x in dp:
    for d in x:
        print(d)
    print()

for i in range(len(dp) - 1):
    a = num[i]
    print(a)
    for left in range(5):
        for right in range(5):
            print(left, right)
            dp[i + 1][left][a] = min(dp[i + 1][left][a], dp[i][left][right] + dist(right, a))
            dp[i + 1][a][right] = min(dp[i + 1][a][right], dp[i][left][right] + dist(left, a))

    for x in dp:
        for d in x:
            print(d)
        print()
    print()

print(min(map(min, dp[len(dp) - 1])))
