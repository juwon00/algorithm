import heapq
import sys

input = sys.stdin.readline

INF = sys.maxsize

n, m, k = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[b].append((a, c))

interview = list(map(int, input().split()))

print(graph)
print(interview)


def dijkstra():
    q = []
    distance = [INF] * (n + 1)
    # distance[start] = 0
    # heapq.heappush(q, (0, start))

    for i in interview:
        heapq.heappush(q, (0, i))
        distance[i] = 0

    while q:
        dist, now = heapq.heappop(q)
        print("dist", dist, "now", now)

        if dist > distance[now]:
            continue

        for x, y in graph[now]:
            print(x, y)
            cost = dist + y

            if cost < distance[x]:
                print("low")
                distance[x] = cost
                heapq.heappush(q, (cost, x))

    return distance


distance = dijkstra()
print(distance)
max_start, max_cost = 0, 0

for i in range(1, n + 1):
    if max_cost < distance[i]:
        max_start, max_cost = i, distance[i]

print(max_start)
print(max_cost)

# 나는 면접장에서 부터 각 도시까지 거리를 다 계산하고, 그중 최소거리를 구하는 방식으로 접근했다
# 하지만 시간초과가 나서 아래 코드를 수정했다
# 면접장을 큐에 한번에 넣고 돌리면 최소 거리가 나온다 (?) - 모든면접장에서 한번에 출발하는 느낌
#
# total_distance = []
# for i in interview:
#     total_distance.append(dijkstra(i))
# print(total_distance)
#
# dis = []
# for i in range(1, n + 1):
#     print(i)
#     tmp = []
#     for j in range(k):
#         print("j", j)
#         tmp.append(total_distance[j][i])
#     print(tmp)
#     d = min(tmp)
#     dis.append((i, d))
# print(dis)
#
# dis.sort(key=lambda x: (-x[1], x[0]))
# print(dis)
#
# print(dis[0][0])
# print(dis[0][1])
