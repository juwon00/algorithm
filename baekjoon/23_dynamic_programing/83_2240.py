t, w = map(int, input().split())
arr = []
for _ in range(t):
    arr.append(int(input()))
print(arr)

dp = [[0] * (w + 2) for _ in range(t + 1)]
if arr[0] == 1:
    dp[1][1], dp[1][2] = 1, 0
else:
    dp[1][1], dp[1][2] = 0, 1

for d in dp:
    print(d)

for i in range(2, t + 1):
    print(i)
    for j in range(1, w + 2):
        print(i, j)
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1])
        if j % 2 == 0 and arr[i - 1] == 2:
            dp[i][j] += 1
        elif j % 2 == 1 and arr[i - 1] == 1:
            dp[i][j] += 1

    for d in dp:
        print(d)

print(max(dp[-1]))

# dp[i][j] = dp[시간][이동 횟수]
