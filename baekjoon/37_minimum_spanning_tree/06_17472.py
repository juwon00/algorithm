# DFS로 섬의 개수 찾고
# 가능한 모든 다리를 구해서
# MST로 다리의 총 길이를 구했습니다.

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return

    if graph[x][y] == 1:
        graph[x][y] = island + 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())

graph = []
for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

for gr in graph:
    print(gr)

island = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            print("find")
            island += 1
            dfs(i, j)
print(island)
for gr in graph:
    print(gr)

edges = []
for i in range(n):
    for j in range(m):
        if graph[i][j] > 0:
            print("x, y:", i, j)
            for k in range(4):
                cost = 0
                nx = i + dx[k]
                ny = j + dy[k]
                if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                    continue
                if graph[nx][ny] != 0:
                    continue
                print(nx, ny)
                while True:
                    nx = nx + dx[k]
                    ny = ny + dy[k]

                    if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                        break

                    cost += 1

                    if graph[nx][ny] == 0:
                        continue

                    if graph[nx][ny] > 0:
                        print("bridge")
                        if cost > 1:
                            if graph[i][j] != graph[nx][ny]:  # 처음에 생각하지 못했던 부분 1 - 반례1과 같이 같은 섬을 있는 다리가 있을 때
                                print(graph[i][j] - 1, graph[nx][ny] - 1, "====")
                                edges.append((cost, graph[i][j] - 1, graph[nx][ny] - 1))
                        break
                print(cost)

edges.sort()
print(edges)

result = 0
parent = [i for i in range(island + 1)]
for i in range(len(edges)):
    cost, a, b = edges[i]
    if find_parent(parent, a) != find_parent(parent, b):
        result += cost
        union_parent(parent, a, b)
        print(a, b, parent)

for i in range(len(parent)):  # 처음에 생각하지 못했던 부분 2 - 반례2와 같이 parent가 갱신 안될때가 있는 경우
    parent[i] = find_parent(parent, i)
print(parent)

parent_set = set(parent)

if len(parent_set) > 2:
    print(-1)
else:
    print(result)

# 반례 1
# 2 7
# 1 0 0 0 1 0 1
# 1 1 1 1 1 0 1


# 반례 2
# 8 6
# 0 1 0 0 1 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 1 0 0 1 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 1 1 1 1 0
# parent = [0, 1, 1, 1, 3, 3]
