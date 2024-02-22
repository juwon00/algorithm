import heapq

INF = int(1e9)

cnt = 1
while True:
    n = int(input())

    if n == 0:
        break

    cave = []
    for _ in range(n):
        cave.append(list(map(int, input().split())))

    # for a in range(n):
    #     print(cave[a])
    # print()

    q = []
    distance = [[INF] * n for _ in range(n)]
    distance[0][0] = cave[0][0]
    heapq.heappush(q, (distance[0][0], (0, 0)))

    # for b in range(n):
    #     print(distance[b])
    # print()

    while q:
        dist, now = heapq.heappop(q)
        # print("dist", dist, "now", now)

        north = tuple(sum(elem) for elem in zip(now, (-1, 0)))
        east = tuple(sum(elem) for elem in zip(now, (0, 1)))
        south = tuple(sum(elem) for elem in zip(now, (1, 0)))
        west = tuple(sum(elem) for elem in zip(now, (0, -1)))

        for i in [north, east, south, west]:
            # print(i)
            if 0 <= i[0] < n and 0 <= i[1] < n:
                # print("good", i)
                cost = dist + cave[i[0]][i[1]]
                # print("cost", cost)

                if cost < distance[i[0]][i[1]]:
                    distance[i[0]][i[1]] = cost
                    heapq.heappush(q, (cost, (i[0], i[1])))

    # for b in range(n):
    #     print(distance[b])
    # print()
    print("Problem", cnt, end="")
    print(":", distance[n - 1][n - 1])
    cnt += 1
