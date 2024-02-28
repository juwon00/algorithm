n = int(input())
graph = []
for i in range(n):
    graph.append([0] + list(map(int, input().split())) + [0])
for g in graph:
    print(g)

if n == 1:
    print(graph[0][1])
    exit()

for i in range(1, n):
    for j in range(1, len(graph[i]) - 1):
        graph[i][j] += max(graph[i - 1][j], graph[i - 1][j - 1])

    for g in graph:
        print(g)

    if i == n - 1:
        print(max(graph[i]))
