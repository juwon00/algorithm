import sys

input = sys.stdin.readline


def dfs(x, y, value, depth, visited):
    global answer

    if visited[x][y]:
        return

    if depth == 4:
        print(">", x, y, value, depth)
        print("value", value)
        answer = max(answer, value)
        return

    print(">", x, y, value, depth)
    visited[x][y] = True

    for v in visited:
        print(v)
    print()
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            dfs(nx, ny, value + graph[nx][ny], depth + 1, visited)

    visited[x][y] = False


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
for g in graph:
    print(g)
answer = 0

for i in range(n):
    for j in range(m):
        print(i, j)
        visited = [[False for _ in range(m)] for _ in range(n)]
        dfs(i, j, graph[i][j], 1, visited)
        print("answer", answer)
        print()
print(">>>>>>>>>>>>")

shapes = [[(0, 1), (0, 2), (1, 1)], [(0, 1), (-1, 1), (1, 1)], [(0, 1), (0, 2), (-1, 1)], [(0, -1), (1, -1), (-1, -1)]]

for i in range(n):
    for j in range(m):
        print(i, j)
        for shape in shapes:
            # print(shape)
            pos = []
            for dx, dy in shape:
                pos.append((i + dx, j + dy))
            if pos[0][0] < 0 or pos[0][0] >= n or pos[0][1] < 0 or pos[0][1] >= m:
                continue
            elif pos[1][0] < 0 or pos[1][0] >= n or pos[1][1] < 0 or pos[1][1] >= m:
                continue
            elif pos[2][0] < 0 or pos[2][0] >= n or pos[2][1] < 0 or pos[2][1] >= m:
                continue
            print(pos)
            tmp = graph[pos[0][0]][pos[0][1]] + graph[pos[1][0]][pos[1][1]] + graph[pos[2][0]][pos[2][1]]
            answer = max(answer, graph[i][j] + tmp)

print(answer)
