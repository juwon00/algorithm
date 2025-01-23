def bf(start):
    dist[start] = 0
    for i in range(n):
        print(i)
        for j in range(len(edges)):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            if dist[next_node] > dist[cur] + cost:  # and dist[cur] != INF - 처음에 적용했다가 실패: 1번 정점에서 도달 가능한 음수 사이클만을 탐지
                dist[next_node] = dist[cur] + cost
                print(cur, next_node, dist)
                if i == n - 1:
                    return True
    return False


INF = int(1e9)

tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())
    edges = []
    dist = [INF] * (n + 1)

    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    print("edges:", edges)

    negative_cycle = bf(1)
    print("final dist:", dist)

    if negative_cycle:
        print("YES")
    else:
        print("NO")
