import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(vertex, dist):
    for v, d in graph[vertex]:
        cal_dist = dist + d
        if visited[v] == -1:
            visited[v] = cal_dist
            dfs(v, cal_dist)


v = int(input())
graph = [[] for _ in range(v + 1)]
print(graph)
for _ in range(v):
    li = list(map(int, input().split()))
    li.pop(-1)
    node = li.pop(0)
    print(node, li)
    while li:
        edge = li.pop(0)
        vertex = li.pop(0)
        graph[node].append((edge, vertex))

print(graph)
visited = [-1] * (v + 1)
visited[1] = 0
dfs(1, 0)
print(visited)

index = visited.index(max(visited))
# index, long_vertex = 0, 0
# for i, visit in enumerate(visited):
#     if visit > long_vertex:
#         long_vertex = visit
#         index = i
print(index)

visited = [-1] * (v + 1)
visited[index] = 0
dfs(index, 0)
print(visited)
print(max(visited))

