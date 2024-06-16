import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(x, y):
    print("in", x, y)
    tmp = 1
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and graph[x][y] < graph[nx][ny]:
            if dp[nx][ny] == 0:
                print(0)
                tmp = max(tmp, dfs(nx, ny) + 1)
            else:
                print("+")
                tmp = max(tmp, dp[nx][ny] + 1)
    print("out", x, y)
    dp[x][y] = tmp
    return dp[x][y]


# 기존에 시간 초과가 생겼던 코드
# 기존 코드는 (x,y) 까지 오는 최대 일 수, 바꾼 코드는 (x,y) 부터 살 수 있는 최대 일 수
# def dfs(x, y, dist):
#     global answer
#     dp[x][y] = dist
#     answer = max(answer, dist)
#
#     for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < n and 0 <= ny < n and graph[x][y] < graph[nx][ny] and dp[nx][ny] < dist + 1:
#             dfs(nx, ny, dist + 1)


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
answer = 0

for g in graph:
    print(g)
print()
for d in dp:
    print(d)
print()

for i in range(n):
    for j in range(n):
        if dp[i][j] == 0:
            print(">>>>", i, j)
            answer = max(answer, dfs(i, j))

            for d in dp:
                print(d)
            print()

print(answer)
