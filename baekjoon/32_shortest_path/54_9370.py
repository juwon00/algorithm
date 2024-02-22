import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)


def dijkstra(start):
    q = []
    distance = [INF] * (n + 1)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        print("dist", dist, "now", now)

        if dist > distance[now]:
            print("continue")
            continue

        for x, y in graph[now]:
            print(x, y)
            cost = dist + y

            if cost < distance[x]:
                print("low")
                distance[x] = cost
                heapq.heappush(q, (cost, x))

    print(distance)
    return distance


test = int(input())

for _ in range(test):
    n, m, t = map(int, input().split())

    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    x_list = []
    for _ in range(t):
        x_list.append(int(input()))

    print(graph)
    print(x_list)

    first_distance = dijkstra(s)
    min_dist = min(first_distance[g], first_distance[h])
    print(min_dist)

    if min_dist == first_distance[g]:
        first_stopover = g
        second_stopover = h
    elif min_dist == first_distance[h]:
        first_stopover = h
        second_stopover = g
    print(first_stopover, second_stopover)

    print("========================")
    second_distance = dijkstra(second_stopover)

    second_dist = min_dist + second_distance[first_stopover]

    result = []
    for x in x_list:
        print(x)
        total_dist = second_dist + second_distance[x]
        print(total_dist)
        if total_dist <= first_distance[x]:
            print("here")
            result.append(x)

    result.sort()
    print(*result)
