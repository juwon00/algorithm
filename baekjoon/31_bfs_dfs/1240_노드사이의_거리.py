from collections import deque


def bfs(x, y, graph, visited):
    q = deque()
    q.append((x, 0))

    while q:
        now, distance = q.popleft()
        print("now, distance", now, distance)
        if now == y:
            return distance

        for node, dis in graph[now]:
            if not visited[node]:
                print(now, node, dis)
                visited[node] = True
                q.append((node, distance + dis))


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
print(graph)

for _ in range(m):
    x, y = map(int, input().split())
    visited = [False] * (n + 1)
    visited[x] = True
    print(bfs(x, y, graph, visited))
