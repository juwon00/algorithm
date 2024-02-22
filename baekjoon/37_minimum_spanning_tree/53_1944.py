import sys
from collections import deque

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(start_x, start_y, goal_x, goal_y):
    queue = deque()
    queue.append((start_x, start_y, 0))
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[start_x][start_y] = True

    while queue:
        print(queue)
        x, y, cost = queue.popleft()
        cost += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx == goal_x and ny == goal_y:
                print("find", cost)
                return cost

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and maze[nx][ny] != '1':
                print("go", nx, ny, cost)
                visited[nx][ny] = True
                queue.append((nx, ny, cost))
    return -1


n, m = map(int, input().split())
maze = []
for _ in range(n):
    tmp = list(input())
    maze.append(tmp)

keys = []
for i in range(n):
    for j in range(n):
        if maze[i][j] == "S" or maze[i][j] == "K":
            keys.append((i, j))
print(keys)

edges = []
for i in range(m + 1):
    for j in range(i + 1, m + 1):
        sx, sy = keys[i]
        gx, gy = keys[j]
        cost = bfs(sx, sy, gx, gy)
        if cost > 0:
            edges.append((cost, i, j))
edges.sort()
print(edges)

result = 0
parent = [i for i in range(m + 1)]
for i in range(len(edges)):
    cost, a, b = edges[i]
    if find_parent(parent, a) != find_parent(parent, b):
        result += cost
        union_parent(parent, a, b)

print(parent)
for i in range(m + 1):
    parent[i] = find_parent(parent, i)

if len(set(parent)) > 1:
    print(-1)
else:
    print(result)
