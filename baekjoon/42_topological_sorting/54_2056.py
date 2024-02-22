from collections import deque
import sys

input = sys.stdin.readline


def topological_sort():
    dp = [0] * (n + 1)
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = time[i]

    while q:
        now = q.popleft()
        print("now", now)

        for j in graph[now]:

            dp[j] = max(dp[j], time[j] + dp[now])
            indegree[j] -= 1

            if indegree[j] == 0:
                q.append(j)
    print(max(dp))


n = int(input())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
time = [0]
for a in range(n):
    tmp = list(map(int, input().split()))
    time.append(tmp[0])
    for b in tmp[2:]:
        graph[b].append(a + 1)
        indegree[a + 1] += 1

print(time)
print(graph)
print(indegree)

topological_sort()
