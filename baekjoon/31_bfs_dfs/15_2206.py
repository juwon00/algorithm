from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
for g in graph:
    print(g)

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y, 0))

    while q:
        print()

        x, y, break_cnt = q.popleft()
        print(x, y, break_cnt)
        print(q)
        for v in visited:
            print(v)

        if x == n - 1 and y == m - 1:
            return visited[x][y][break_cnt]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 1 and break_cnt == 0:
                print("부숨", nx, ny)
                visited[nx][ny][1] = visited[x][y][0] + 1
                q.append((nx, ny, 1))

            elif graph[nx][ny] == 0 and visited[nx][ny][break_cnt] == 0:
                print("안부숨", nx, ny)
                visited[nx][ny][break_cnt] = visited[x][y][break_cnt] + 1
                q.append((nx, ny, break_cnt))

    return -1


print(bfs(0, 0))
