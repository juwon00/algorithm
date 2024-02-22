# 기존의 위상정렬에서 쓰는 deque가 아닌 heapq를 써서 queue에서 최솟값을 꺼낼 수 있도록 한다.

import heapq
import sys

input = sys.stdin.readline


def topological_sorting():
    result = []
    q = []
    for j in range(1, n + 1):
        if indegree[j] == 0:
            heapq.heappush(q, j)
    print(q)

    while q:
        now = heapq.heappop(q)
        print(now)
        result.append(now)

        for j in graph[now]:
            indegree[j] -= 1
            if indegree[j] == 0:
                heapq.heappush(q, j)
    print(*result)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
print(graph)
print(indegree)

topological_sorting()
