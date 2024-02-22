from collections import deque
import sys

input = sys.stdin.readline


def topological_sort():
    q = deque()
    result = [0] * (n + 1)

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            result[i] = time[i]

    while q:
        now = q.popleft()
        print("now", now)

        for j in graph[now]:
            print(j)
            indegree[j] -= 1
            result[j] = max(result[j], time[j] + result[now])  # dp와 결합된 문제가 자주 나오려나

            if indegree[j] == 0:
                q.append(j)

    for r in range(1, n + 1):
        print(result[r])


n = int(input())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
time = [0]

for i in range(n):
    tmp = list(map(int, input().split()))
    print(tmp)
    time.append(tmp[0])
    for j in range(1, len(tmp) - 1):
        print(i + 1, tmp[j])
        graph[tmp[j]].append(i + 1)
        indegree[i + 1] += 1
print(time)
print(graph)
print(indegree)

topological_sort()
