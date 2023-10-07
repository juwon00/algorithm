from collections import deque


def bfs():
    queue = deque()
    for i in range(n*h):
        for j in range(m):
            if tomato[i][j] == 1:
                # print("i, j:", i, j)
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        # print(x, y)

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n*h or ny < 0 or ny >= m:
                continue
            if i == 0 or i == 1:  # 주의할 부분! 위아래로 움직일때 층이 같지 않으면 안된다!
                if x // n != nx // n:
                    continue
            if tomato[nx][ny] == 0:
                if not visited[nx][ny]:
                    # print("nx, ny:", nx, ny)
                    tomato[nx][ny] = tomato[x][y] + 1
                    queue.append((nx, ny))
                    visited[nx][ny] = True


m, n, h = map(int, input().split())

tomato = []
for i in range(n*h):
    tomato.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0, n, -n]
dy = [0, 0, -1, 1, 0, 0]

visited = [[False for _ in range(m)] for _ in range(n*h)]

bfs()

# for l in range(n*h):
#     print(tomato[l])


if any(0 in l for l in tomato):
    print(-1)
else:
    print(max(map(max, tomato)) - 1)
