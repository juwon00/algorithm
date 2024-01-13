from collections import deque
import sys

input = sys.stdin.readline


def topological_sort():
    q = deque()
    result = []
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


t = int(input())

for _ in range(t):
    n = int(input())
    team = list(map(int, input().split()))

    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for i in range(n):
        for j in range(i + 1, n):
            print(i, j, team[i], team[j])
            graph[team[i]].append(team[j])
            indegree[team[j]] += 1

    print(team)
    print(indegree)
    print(graph)

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        print(a, b)

        if b in graph[a]:
            graph[b].append(a)
            graph[a].remove(b)
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a].append(b)
            graph[b].remove(a)
            indegree[b] += 1
            indegree[a] -= 1

    print(graph)
    print(indegree)

    result = topological_sort()
    print(*result)
    if len(result) == n:
        print(*result)
    else:
        print("IMPOSSIBLE")
