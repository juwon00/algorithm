# Dijkstra 알고리즘을 사용한 풀이

import heapq

INF = int(1e9)


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)

    for i in range(len(edge)):
        a, b, c = edge[i][0], edge[i][1], 1
        graph[a].append((b, c))
        graph[b].append((a, c))
    print(graph)

    start = 1
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        print(dist, now)
        print(distance)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            print(i, cost)

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    distance.pop(0)
    print(distance)
    print(distance.count(max(distance)))
    return distance.count(max(distance))


n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
solution(n, edge)
