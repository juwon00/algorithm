from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))
print(n, m)
for g in graph:
    print(g)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            a, b = i, j
            break
print(a, b)

q = deque()
q.append((a, b))
visited = [[False] * m for _ in range(n)]

result = 0
while q:
    x, y = q.popleft()
    print(x, y)
    for v in visited:
        print(v)
    print()

    if graph[x][y] == 'P':
        result += 1

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and (graph[nx][ny] == 'O' or graph[nx][ny] == 'P'):
            q.appendleft((nx, ny))
            visited[nx][ny] = True

if result == 0:
    print("TT")
else:
    print(result)
