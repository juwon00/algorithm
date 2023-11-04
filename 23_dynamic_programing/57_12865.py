n, k = map(int, input().split())
w = []
v = []
w.append(0)
v.append(0)
for i in range(n):
    ww, vv = map(int, input().split())
    w.append(ww)
    v.append(vv)

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    print(w, v)
    for j in range(1, k + 1):
        print(i, j)
        if w[i] > j:
            print("-")
            dp[i][j] = dp[i - 1][j]
        else:
            print("====", dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])
    print()
    for a in range(n + 1):
        print(dp[a])
    print()

print(dp[-1][-1])
