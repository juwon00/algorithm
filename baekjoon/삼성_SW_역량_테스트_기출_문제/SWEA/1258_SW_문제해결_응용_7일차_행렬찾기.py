from collections import deque


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    metrix = [(x, y)]
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] != 0:
                visited[nx][ny] = True
                metrix.append((nx, ny))
                q.append((nx, ny))
    metrix.sort()
    # print(metrix)
    lu_x, lu_y = metrix[0]
    rd_x, rd_y = metrix[-1]
    w = rd_x - lu_x + 1
    h = rd_y - lu_y + 1
    return w, h


for t in range(int(input())):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    count = 0
    square = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0 and not visited[i][j]:
                count += 1
                w, h = bfs(i, j)
                # print(w, h)
                square.append((w, h))
                # for v in visited:
                #     print(v)
                # print()
    square.sort(key=lambda x: (x[0] * x[1], x[0]))
    print(f"#{t + 1} {count} ", end="")
    print(" ".join(f"{x} {y}" for x, y in square))
