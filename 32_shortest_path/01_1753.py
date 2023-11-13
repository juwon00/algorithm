import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # a번 노드에서 b번 노드로 가는 비용이 c라는 의미

print(graph)
print(distance)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        print(q)
        dist, now = heapq.heappop(q)
        print("dist now:", dist, now)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            print(i)
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                print("change", distance)
                heapq.heappush(q, (cost, i[0]))


dijkstra(k)
print()
print(graph)
print(distance)

for i in range(1, v + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
