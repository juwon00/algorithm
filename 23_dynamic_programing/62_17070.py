n = int(input())

house = [[0] * (n + 1)]
for i in range(n):
    house.append([0])
    house[i + 1].extend(list(map(int, input().split())))

for a in range(n + 1):
    print(house[a])

print()
dp = [[[0 for _ in range(4)] for _ in range(n + 1)] for _ in range(n + 1)]
dp[1][2][2] = 1
dp[1][2][3] = 1
for a in range(n + 1):
    print(dp[a])

print()
print()
for i in range(1, n + 1):
    for j in range(3, n + 1):
        print(i, j)
        if house[i][j] == 1:
            continue

        print(dp[i-1][j-1][3], dp[i-1][j][3] - dp[i-1][j][2], dp[i][j-1][3] - dp[i][j-1][1])
        dp[i][j][0] = dp[i-1][j-1][3]
        dp[i][j][1] = dp[i-1][j][3] - dp[i-1][j][2]
        dp[i][j][2] = dp[i][j-1][3] - dp[i][j-1][1]

        if house[i-1][j] == 1:
            print("up")
            dp[i][j][0] = 0
        if house[i][j-1] == 1:
            print("left")
            dp[i][j][0] = 0

        print(dp[i][j][0] + dp[i][j][1] + dp[i][j][2])
        dp[i][j][3] = dp[i][j][0] + dp[i][j][1] + dp[i][j][2]

        for a in range(n + 1):
            print(dp[a])

print()
for a in range(n + 1):
    print(dp[a])

print(dp[n][n][3])
