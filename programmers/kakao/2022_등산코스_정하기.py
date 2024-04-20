# 다시 풀어볼 문제

import heapq
from math import inf


def solution(n, paths, gates, summits):
    answer = []
    graph = [[] for _ in range(n + 1)]
    for now, next, w in paths:
        graph[now].append([next, w])
        graph[next].append([now, w])
    print(graph)

    # 산봉우리 판별
    is_summit = [False] * (n + 1)
    for summit in summits:
        is_summit[summit] = True

    # gates 모두 시작 위치
    distance = [inf] * (n + 1)
    q = []
    for gate in gates:
        distance[gate] = 0
        heapq.heappush(q, [0, gate])
    print(is_summit)
    print(distance)
    print(q)
    print()

    # 다익스트라
    while q:
        dist, now = heapq.heappop(q)
        print("dist now", dist, now)
        print(distance)

        # 산봉우리면 바로 continue
        # 이렇게 해야 두 개 이상의 산봉우리를 방문하지 않는다.
        if distance[now] < dist or is_summit[now]:
            print("continue")
            print()
            continue

        for next, next_dist in graph[now]:
            next_dist = max(distance[now], next_dist)
            print("next", next_dist, next)
            if distance[next] > next_dist:
                print("-> push")
                distance[next] = next_dist
                heapq.heappush(q, [next_dist, next])
            print()
        print()

    result = [-1, inf]
    summits = sorted(summits)
    for summit in summits:
        print(summit)
        if distance[summit] < result[1]:
            result[0] = summit
            result[1] = distance[summit]

    return result


n = 6
paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
gates = [1, 3]
summits = [5]
answer = solution(n, paths, gates, summits)
print("answer:", answer)
