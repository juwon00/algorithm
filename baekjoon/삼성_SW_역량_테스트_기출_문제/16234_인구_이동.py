from collections import deque


def bfs(i, j, visited):
    result = []
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()

        if visited[x][y]:
            continue
        print("now", x, y)
        visited[x][y] = True
        result.append((x, y))

        # 북, 남, 서, 동
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                    q.append((nx, ny))

    print("finish")
    return result


n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
for g in graph:
    print(g)

answer = 0
while True:
    visited = [[False] * n for _ in range(n)]
    unions = []
    for i in range(n):
        for j in range(n):
            print(graph[i][j])
            if not visited[i][j]:
                print("bfs start")
                unions.append(bfs(i, j, visited))
            print()

    print("unions", unions)
    if len(unions) == n * n:
        break
    for union in unions:
        print(union)
        tmp = 0
        for u in union:
            tmp += graph[u[0]][u[1]]
        print(tmp // len(union))
        tmp = tmp // len(union)
        for u in union:
            graph[u[0]][u[1]] = tmp

    for g in graph:
        print(g)
    answer += 1

print(answer)
