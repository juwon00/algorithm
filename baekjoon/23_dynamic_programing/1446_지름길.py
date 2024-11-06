n, d = map(int, input().split())
shortcut = []
for _ in range(n):
    shortcut.append(list(map(int, input().split())))
shortcut.sort()
print(shortcut)

dp = [i for i in range(10001)]

for start, end, cost in shortcut:
    for j in range(10001):
        # print(dp[j])
        if j == start:
            dp[end] = min(dp[end], dp[start] + cost)
        dp[j] = min(dp[j], dp[j - 1] + 1)

# for x in enumerate(dp[:151]):
#     print(x)
print(dp[d])
