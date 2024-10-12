from collections import deque

n, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, x = map(int, input().split())
    graph[a].append((b, x))
    graph[b].append((a, x))
print(graph)


def bfs(k, start):
    q = deque()
    q.append(start)
    visited = [False] * (n + 1)
    visited[start] = True
    print()
    print("K", k)
    cnt = 0
    while q:
        now = q.popleft()
        print("now", now)

        for node, usado in graph[now]:
            print(node, usado)
            if usado >= k and not visited[node]:
                visited[node] = True
                q.append(node)
                cnt += 1
    return cnt




for _ in range(q):
    k, v = map(int, input().split())
    print(bfs(k, v))
    print()