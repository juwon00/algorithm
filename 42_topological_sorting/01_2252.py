from collections import deque
import sys

input = sys.stdin.readline


def topological_sort():
    result = []
    q = deque()  # 큐를 이용한 위상정렬
    for i in range(1, n + 1):  # 진입차수가 0인 노드 q에 삽입
        if indegree[i] == 0:
            q.append(i)
    print(q)

    while q:
        now = q.popleft()
        result.append(now)
        print("now", now)

        for i in graph[now]:  # 이어진 간선들 하나씩 없애기
            print(i)
            indegree[i] -= 1

            if indegree[i] == 0:  # -1씩 하다가 진입차수 0이 되면 q에 삽입
                q.append(i)
    print(*result)


n, m = map(int, input().split())

indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

print(indegree)
print(graph)

topological_sort()
