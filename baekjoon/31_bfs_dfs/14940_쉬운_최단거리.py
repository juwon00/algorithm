from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
start_x, start_y = -1, -1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start_x, start_y = i, j
            break
    if start_x != -1 and start_y != -1:
        break

q = deque()
visited = [[False] * m for _ in range(n)]
q.append((start_x, start_y, 0))
visited[start_x][start_y] = True
graph[start_x][start_y] = 0
while q:
    x, y, cnt = q.popleft()
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and not visited[nx][ny]:
            visited[nx][ny] = True
            graph[nx][ny] = cnt + 1
            q.append((nx, ny, cnt + 1))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            graph[i][j] = -1

for g in graph:
    print(*g)