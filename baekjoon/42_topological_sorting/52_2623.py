from collections import deque
import sys

input = sys.stdin.readline


def topological_sort():
    result = []
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)
    return result


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    tmp = list(map(int, input().split()))
    size = tmp[0]
    order = tmp[1:]
    print(size, order)

    for i in range(size):
        for j in range(i + 1, size):
            print(i, j, "  ", order[i], order[j])
            graph[order[i]].append(order[j])
            indegree[order[j]] += 1

print(graph)
print(indegree)

result = topological_sort()
if len(result) == n:
    print(*result)
else:
    print(0)