import heapq

INF = int(1e9)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        print("dist, now", dist, now)
        print(distance)

        if distance[now] < dist:
            continue

        for next, cost in graph[now]:
            print(next, cost)
            if dist + cost < distance[next]:
                distance[next] = dist + cost
                heapq.heappush(q, (dist + cost, next))


n = int(input())
m = int(input())
distance = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]
print(graph)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())
print(graph)
print(start, end)

dijkstra(start)

print(distance[end])
