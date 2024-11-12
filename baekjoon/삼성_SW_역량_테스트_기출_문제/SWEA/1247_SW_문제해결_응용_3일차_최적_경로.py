from itertools import permutations


def dfs(start, end, houses):
    min_distance = int(1e9)

    for perm in permutations(houses):
        path = [start] + list(perm) + [end]
        # print(path)
        dist = 0

        for i in range(len(path) - 1):
            dist += abs(path[i][0] - path[i + 1][0]) + abs(path[i][1] - path[i + 1][1])
            # print(dist)
        min_distance = min(min_distance, dist)
        # print("min_distance", min_distance)
    return min_distance


for t in range(int(input())):
    n = int(input())
    graph = list(map(int, input().split()))
    com_x, com_y = graph[0], graph[1]
    home_x, home_y = graph[2], graph[3]
    houses = []
    for i in range(4, n * 2 + 4, 2):
        houses.append((graph[i], graph[i + 1]))
    print(com_x, com_y)
    print(home_x, home_y)
    print(houses)

    result = dfs((com_x, com_y), (home_x, home_y), houses)
    print(f"#{t + 1} {result}")
    print()
