def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def solution(n, computers):
    for c in computers:
        print(c)
    visited = [False] * n
    graph = [[] for _ in range(n)]
    print(graph)
    for i in range(n):
        for j in range(i, n):
            if i == j:
                continue
            print(i, j)

            if computers[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)
    print(graph)
    print(visited)

    answer = 0
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(graph, i, visited)
    print(answer)

    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
solution(n, computers)
