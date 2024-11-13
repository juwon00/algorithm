import heapq

for t in range(int(input())):
    n = int(input())

    # graph = []
    # for _ in range(n):
    #     graph.append(list(input()))
    # for i in range(n):
    #     for j in range(n):
    #         graph[i][j] = int(graph[i][j])
    # 위의 코드를 좀 더 Pythonic하게 만든것
    graph = [list(map(int, input())) for _ in range(n)]

    # for i in range(n):
    #     for j in range(n):
    #         if i == 0 and j == 0:
    #             continue
    #         elif i == 0:
    #             graph[i][j] += graph[i][j - 1]
    #         elif j == 0:
    #             graph[i][j] += graph[i - 1][j]
    #         else:
    #             graph[i][j] += min(graph[i][j - 1], graph[i - 1][j])
    # 오른쪽, 아래쪽으로 내려오는 것만으로 풀면 아래와 같은 케이스에 대해서 틀리게 된다
    # 0 9 9 9 9
    # 0 9 9 9 9
    # 0 1 0 0 0
    # 0 1 0 9 0
    # 0 0 0 9 0
    heap = []
    heapq.heappush(heap, (0, 0, 0))
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True

    result = 0
    while heap:
        cost, x, y = heapq.heappop(heap)
        # print(x, y, cost)
        if x == n - 1 and y == n - 1:
            result = cost
            break

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                heapq.heappush(heap, (cost + graph[nx][ny], nx, ny))
    # for g in graph:
    #     print(g)
    print(f"#{t + 1} {result}")
