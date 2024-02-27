import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def dfs(graph, v, visited):
    global cnt
    visited[v] = True
    print(v)
    result[v] = cnt
    cnt += 1

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited,)


n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = [0] * (n + 1)
cnt = 1

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(graph)
for i in range(n + 1):
    graph[i].sort()
print(graph)

dfs(graph, r, visited)
print(result)
for i in range(1, n + 1):
    print(result[i])
