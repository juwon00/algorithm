n, t = map(int, input().split())
study = [[0, 0]]
for i in range(n):
    study.append(list(map(int, input().split())))
study.sort()
print(n, t)
for s in study:
    print(s)

dp = [[0] * (t + 1) for _ in range(n + 1)]
for d in dp:
    print(d)

dist = 0
for i in range(1, n + 1):
    dist += study[i][0]
    print("dist", dist)
    for j in range(1, t + 1):
        print(i, j)
        if j > dist:
            dp[i][j] = dp[i][j - 1]
        elif j - study[i][0] >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - study[i][0]] + study[i][1])
        else:
            dp[i][j] = dp[i - 1][j]
    for d in dp:
        print(d)

print(dp[-1][-1])
