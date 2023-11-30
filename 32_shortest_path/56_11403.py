# 플로이드-워셜

INF = int(100)

n = int(input())

graph = []
for _ in range(n):
    a = list(map(int, input().split()))
    graph.append(a)

for a in range(n):
    for b in range(n):
        if graph[a][b] == 0:
            graph[a][b] = INF

# for w in range(len(graph)):
#     print(graph[w])

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

print()
for w in range(len(graph)):
    print(graph[w])

result = [[0] * n for _ in range(n)]
for a in range(n):
    for b in range(n):
        if graph[a][b] > 0 and graph[a][b] != INF:
            result[a][b] = 1
print()
for w in range(len(result)):
    print(*result[w])
