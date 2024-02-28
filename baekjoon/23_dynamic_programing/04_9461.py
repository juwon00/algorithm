t = int(input())
for _ in range(t):
    n = int(input())

    graph = [0] * 101
    graph[1] = 1
    graph[2] = 1
    graph[3] = 1
    graph[4] = 2
    graph[5] = 2

    for i in range(6, n + 1):
        graph[i] = graph[i - 1] + graph[i - 5]
    print(graph)
    print(graph[n])
