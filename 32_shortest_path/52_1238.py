import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
print(graph)


def dijkstra(start):
    q = []
    distance = [INF] * (n + 1)
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        print("dist", dist, "now", now)

        if distance[now] < dist:
            continue

        for x, y in graph[now]:
            print(x, y)
            cost = dist + y

            if cost < distance[x]:
                print("low")
                distance[x] = cost
                heapq.heappush(q, (cost, x))
                print(distance)
    distance[0] = 0
    return distance


go_back_home = dijkstra(x)

for i in range(1, n + 1):
    go_party = dijkstra(i)
    go_back_home[i] += go_party[x]

print(max(go_back_home))
