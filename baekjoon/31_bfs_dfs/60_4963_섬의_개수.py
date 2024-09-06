import sys

sys.setrecursionlimit(10 ** 6)


def dfs(i, j, visited, graph, w, h):
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        nx, ny = i + dx, j + dy
        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and graph[nx][ny] == 1:
            visited[nx][ny] = True
            dfs(nx, ny, visited, graph, w, h)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    visited = [[False] * w for _ in range(h)]  # visited 안쓰고 방문한곳을 0으로 바꿔도 됨

    result = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                dfs(i, j, visited, graph, w, h)
                result += 1

                for v in visited:
                    print(v)
                print()

    print("result")
    print(result)
    print()
