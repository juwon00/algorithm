from collections import deque
import sys

input = sys.stdin.readline


def topological_sort():
    result = [0] * (n + 1)
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            result[i] += 1

    while q:
        now = q.popleft()
        print("now", now)

        for i in graph[now]:
            print(i)
            result[i] = result[now] + 1

            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)
    return result


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
print(graph)
print(indegree)

result = topological_sort()
for i in range(1, n + 1):
    print(result[i], end=" ")
