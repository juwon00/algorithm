from collections import deque
import sys

sys.setrecursionlimit(1000000)

m, n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for g in graph:
    print(g)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx, ny))

print()
for g in graph:
    print(g)

have_zero = False
max_day = 0
for i in range(n):
    max_day = max(max_day, max(graph[i]))
    if 0 in graph[i]:
        have_zero = True

if have_zero:
    print(-1)
else:
    print(max_day - 1)
