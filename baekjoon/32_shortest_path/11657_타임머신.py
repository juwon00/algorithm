def bellman_ford(start):
    distance[start] = 0

    for i in range(n):
        print(i)
        print(edges)
        for cur_node, next_node, cost in edges:
            print(cur_node, next_node, cost)

            if distance[cur_node] != INF and distance[cur_node] + cost < distance[next_node]:
                distance[next_node] = distance[cur_node] + cost

                if i == n - 1:
                    print("음수 순환")
                    return True
        print(distance)
        print()

    return False


INF = int(1e9)

n, m = map(int, input().split())

edges = []
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

flag = bellman_ford(1)

print(distance)

if flag:
    print(-1)
else:
    for index, d in enumerate(distance):
        if index == 0 or index == 1:
            continue
        if d == INF:
            print(-1)
        else:
            print(d)
