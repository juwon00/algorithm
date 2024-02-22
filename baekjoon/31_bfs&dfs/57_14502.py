# 다른 블로그에서 본 아래와 같이 백트래킹을 통해 벽을 세우는 방법이 더 좋을 것 같다.

# def make_wall(count):
#     if count == 3:
#         bfs()
#         return
#     for i in range(n):
#         for k in range(m):
#             if lab_map[i][k] == 0:
#                 lab_map[i][k] = 1
#                 make_wall(count+1)
#                 lab_map[i][k] = 0


from collections import deque
from itertools import combinations

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):

    if lab[i][j] != 0:
        return 0

    queue = deque()
    lab[i][j] = 5
    queue.append((i, j))

    cnt = 1
    visit_2 = False
    while queue:
        x, y = queue.popleft()
        # print("popleft:", x, y)

        for s in range(4):
            nx = x + dx[s]
            ny = y + dy[s]
            # print("nx,ny:", nx, ny)

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if lab[nx][ny] == 1 or lab[nx][ny] == 5:
                continue
            if lab[nx][ny] == 2:
                visit_2 = True
            if lab[nx][ny] == 0:
                # print("append:", nx, ny)
                lab[nx][ny] = 5
                cnt += 1
                queue.append((nx, ny))

    if visit_2:
        # print("visit_2")
        return 0
    else:
        return cnt


n, m = map(int, input().split())
lab = []
for i in range(n):
    lab.append(list(map(int, input().split())))
# for p in range(n):
#     print(lab[p])

wall = []
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            wall.append([i, j])
# print(wall)

wall_combi = list(combinations(wall, 3))

safe = 0
for x, y, z in wall_combi:
    # print(x, y, z)
    lab[x[0]][x[1]], lab[y[0]][y[1]], lab[z[0]][z[1]] = 1, 1, 1

    # for p in range(n):
    #     print(lab[p])
    # print()

    bfs_cnt = 0
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                # print("i,j", i, j)
                bfs_cnt += bfs(i, j)
                if safe < bfs_cnt:
                    safe = bfs_cnt
                # print("safe", safe)

    for i in range(n):
        for j in range(m):
            if lab[i][j] == 5:
                lab[i][j] = 0

    lab[x[0]][x[1]], lab[y[0]][y[1]], lab[z[0]][z[1]] = 0, 0, 0

print(safe)
