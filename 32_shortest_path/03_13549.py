import heapq
import sys

INF = sys.maxsize

n, k = map(int, input().split())

distance = [INF] * 100001


def dijkstra(n, k):
    q = []
    if n >= k:
        print(n - k)
        return

    distance[n] = 0
    heapq.heappush(q, (0, n))
    while q:
        # print(distance)
        dist, now = heapq.heappop(q)
        # print("dist", dist, "now", now)
        for nx in [(now - 1, 1), (now + 1, 1), (now * 2, 0)]:  # 이 부분을 생각못해서 오려걸림 (now*2를 0으로 만드는 부분)
            # print(nx)
            if 0 < nx[0] < 100001 and distance[nx[0]] > dist + nx[1]:
                distance[nx[0]] = dist + nx[1]
                heapq.heappush(q, (distance[nx[0]], nx[0]))

    print(distance[k])


dijkstra(n, k)
