import copy
from collections import deque

import sys
input = sys.stdin.readline


def bfs():
    tmp_graph = copy.deepcopy(graph)

    q = deque()
    for virus in viruses:
        q.append((virus))
    # print(q)

    while q:
        x, y = q.popleft()
        # print("now", x, y)

        # 북 남 서 동
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if tmp_graph[nx][ny] == 0:
                    tmp_graph[nx][ny] = 2
                    q.append((nx, ny))
    result = 0
    for g in tmp_graph:
        # print(g)
        result += g.count(0)
    # print(result)
    return result


def make_wall(cnt):
    global answer

    if cnt == 3:
        answer = max(answer, bfs())
        # for g in graph:
        #     print(g)
        # print()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(cnt + 1)
                graph[i][j] = 0


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# for g in graph:
#     print(g)
# print()

viruses = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            viruses.append((i, j))

answer = 0
make_wall(0)
print(answer)
