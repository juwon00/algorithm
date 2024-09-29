import sys
from collections import defaultdict

input = sys.stdin.readline


def dfs(x, y, cnt):
    global result
    cnt += 1
    result = max(result, cnt)
    print(x, y, graph[x][y])
    print("cnt", cnt)
    print("result", result)
    print(visited)
    print()

    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in visited:
            visited.add(graph[nx][ny])
            dfs(nx, ny, cnt)
            visited.remove(graph[nx][ny])


r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]
# graph = [input() for _ in range(r)]  <- 이렇게 하면 시간초과 발생 왜??
for g in graph:
    print(g)

# visited = defaultdict(bool)
# for i in range(26):
#     visited[chr(i + ord('A'))] = False
# visited[graph[0][0]] = True
# print(visited)
# print()

visited = set(graph[0][0])
result = 0

dfs(0, 0, 0)
print(result)
