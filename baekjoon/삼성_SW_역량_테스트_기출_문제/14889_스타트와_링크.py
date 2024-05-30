# 백트래킹으로도 가능

from itertools import combinations

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
for g in graph:
    print(g)
combi = [0]
combi += list(combinations(range(n), n // 2))
print(combi)
pairs = []
for i in range(1, len(combi) // 2 + 1):
    pairs.append([combi[i], combi[-i]])
print(pairs)

result = int(1e9)
for pair in pairs:
    print("pair", pair)
    ability_x, ability_y = 0, 0
    for x, y in combinations(pair[0], 2):
        ability_x += graph[x][y]
        ability_x += graph[y][x]
    for x, y in combinations(pair[1], 2):
        ability_y += graph[x][y]
        ability_y += graph[y][x]
    print(ability_x, ability_y)
    result = min(result, abs(ability_x - ability_y))
    print()
print(result)
