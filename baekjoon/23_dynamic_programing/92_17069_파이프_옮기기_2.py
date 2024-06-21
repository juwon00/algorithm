n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
for g in graph:
    print(g)
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1
for d in dp:
    print(d)
print()

for x in range(n):
    for y in range(n):
        if (x == 0 and y == 0) or (x == 0 and y == 1) or graph[x][y] == 1:
            continue
        print(">>>>>>>>>>>>>", x, y, dp[x][y])
        for index, d in enumerate([(0, -1), (-1, 0), (-1, -1)]):
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < n:
                print(index, "-", nx, ny, dp[nx][ny])
                if index == 0:
                    dp[x][y][0] = dp[nx][ny][0] + dp[nx][ny][2]
                elif index == 1:
                    dp[x][y][1] = dp[nx][ny][1] + dp[nx][ny][2]
                elif index == 2:
                    if graph[x - 1][y] == 0 and graph[x][y - 1] == 0:
                        dp[x][y][2] = dp[nx][ny][0] + dp[nx][ny][1] + dp[nx][ny][2]
        print()
for d in dp:
    print(d)
print()
print(sum(dp[-1][-1]))
