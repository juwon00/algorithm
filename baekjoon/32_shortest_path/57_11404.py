# 플로이드-워셜
import sys
input = sys.stdin.readline

INF = sys.maxsize

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for w in range(len(graph)):
    print(graph[w])

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0
                continue
            # print(k, a, b)
            # print(graph[a][b], graph[a][k] + graph[k][b])
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            # for w in range(len(graph)):
            #     print(graph[w])
            # print()

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            graph[a][b] = 0

for x in range(1, len(graph)):
    graph[x].pop(0)
    print(*graph[x])
