from collections import deque
import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(graph)
for i in range(n + 1):
    graph[i].sort(reverse=True)
print(graph)

q = deque()
q.append(r)
visited[r] = True
result = [0] * (n + 1)
cnt = 1

while q:
    now = q.popleft()
    result[now] = cnt
    cnt += 1
    print(now, visited, result)

    for i in graph[now]:
        if not visited[i]:
            q.append(i)
            visited[i] = True

print(result)
for i in range(1, n + 1):
    print(result[i])
