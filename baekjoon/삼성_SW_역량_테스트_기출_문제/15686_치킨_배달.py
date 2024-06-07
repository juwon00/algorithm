import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
for g in graph:
    print(g)

house = []
chicken = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append([i, j])
        elif graph[i][j] == 2:
            chicken.append([i, j])
print(house)
print(chicken)

answer = int(1e9)
for c in list(combinations(chicken, m)):
    print(c)
    tmp = 0
    q = deque()
    visited = [[False] * n for _ in range(n)]
    for x, y in c:
        q.append((x, y, 0))
    print(q)
    print()

    while q:
        x, y, dist = q.popleft()
        if visited[x][y]:
            continue
        print("now", x, y, dist)
        visited[x][y] = True

        if graph[x][y] == 1:
            print("find")
            tmp += dist

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                q.append((nx, ny, dist + 1))
    print("tmp", tmp)
    answer = min(tmp, answer)
    print("answer", answer)
print(answer)
