# 처음에 dp를 생각하지 못해서 코드가 꼬였다

from collections import deque
import sys

input = sys.stdin.readline


def topological_sort():
    q = deque()
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = d[i]
    print(q)
    print(dp)

    while q:
        now = q.popleft()
        print("now", now)

        for j in graph[now]:
            print(j)
            indegree[j] -= 1
            dp[j] = max(dp[j], d[j] + dp[now])

            if indegree[j] == 0:
                q.append(j)
        print(dp)
    print(dp[w])


t = int(input())
for _ in range(t):

    n, k = map(int, input().split())
    d = [0] + list(map(int, input().split()))

    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1
    w = int(input())

    print(d)
    print(indegree)
    print(graph)
    print(w)

    topological_sort()
