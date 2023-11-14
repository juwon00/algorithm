import heapq
import sys

input = sys.stdin.readline

INF = sys.maxsize

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())


def dijkstra(start):
    distance = [INF] * (n + 1)

    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        print("dist now", dist, now)

        if dist > distance[now]:
            print("continue")
            continue

        for i in graph[now]:
            print(i)
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance


distance_1 = dijkstra(1)
print()
distance_v1 = dijkstra(v1)
print()
distance_v2 = dijkstra(v2)

print()
print(graph)
print(distance_1)
print(distance_v1)
print(distance_v2)

route1 = distance_1[v1] + distance_v1[v2] + distance_v2[n]
route2 = distance_1[v2] + distance_v2[v1] + distance_v1[n]

print(route1, route2)
result = min(route1, route2)
print(result, "result")
print(INF)

print(result if result < INF else -1)
