def solution(n, s, a, b, fares):
    INF = int(1e9)
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            if x == y:
                graph[x][y] = 0
    for x, y, dist in fares:
        graph[x][y] = dist
        graph[y][x] = dist

    # for g in graph:
    #     print(g)
    # print()

    for k in range(1, n + 1):
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

    for g in graph:
        print(g)
    print()

    answer = graph[s][a] + graph[s][b]
    for i in range(1, n + 1):
        if i != s:
            print(i)
            answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])

    return answer


n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
answer = solution(n, s, a, b, fares)
print("answer:", answer)
