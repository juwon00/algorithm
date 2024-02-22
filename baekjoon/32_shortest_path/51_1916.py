import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (start, 0))

    while q:
        dist, now = heapq.heappop(q)
        print("dist", dist, "now", now)

        if distance[dist] < now:
            continue

        for x, y in graph[dist]:
            print(x, y)

            cost = now + y

            if cost < distance[x]:
                print("low")
                distance[x] = cost
                heapq.heappush(q, (x, cost))


dijkstra(start)
print(distance)
print(distance[end])
