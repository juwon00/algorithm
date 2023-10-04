def dfs__(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == '-':
        graph[x][y] = 'X'
        dfs__(x, y - 1)
        dfs__(x, y + 1)
        return True

    return False


def dfs_l(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == '|':
        graph[x][y] = 'O'
        dfs_l(x - 1, y)
        dfs_l(x + 1, y)
        return True

    return False


n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(str, input())))

result = 0

for i in range(n):
    for j in range(m):
        if dfs__(i, j) == True:
            result += 1

        if dfs_l(i, j) == True:
            result += 1

# print()
# for K in range(n):
#     print(graph[K])

print(result)
