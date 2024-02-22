import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

print(n, m)
print(graph)


def dijkstra(start):
    q = []
    distance = [INF] * (n + 1)
    heapq.heappush(q, (0, start))
    distance[start] = 0
    link = []

    while q:
        dist, now = heapq.heappop(q)
        print("dist", dist, "now", now)

        if dist < distance[now]:
            continue

        for x, y in graph[now]:
            print(x, y)
            cost = dist + y

            if cost < distance[x]:
                print("low")

                for first, last in link:
                    print("= f", first, "l", last)
                    if last == x:
                        print("remove")
                        link.remove((first, last))
                link.append((now, x))

                distance[x] = cost
                heapq.heappush(q, (cost, x))

    print(distance)
    print(link)
    return link


link = dijkstra(1)

print(len(link))
for a in link:
    print(*a)
