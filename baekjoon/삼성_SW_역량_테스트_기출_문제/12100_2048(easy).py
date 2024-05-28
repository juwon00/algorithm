import copy
from collections import deque


def find_next_num(now, x, y, dx, dy):
    nx, ny = x + dx, y + dy
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        return -1
    elif now[nx][ny] > 0:
        tmp = now[nx][ny]
        now[nx][ny] = 0
        return tmp
    elif now[nx][ny] == 0:
        return find_next_num(now, nx, ny, dx, dy)


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
for g in graph:
    print(g)

answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, graph[i][j])

graphs = deque()
graphs.append(graph)

for _ in range(5):

    print("len", len(graphs))
    for _ in range(len(graphs)):

        now_graph = graphs.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

            for ng in now_graph:
                print(ng)

            # 북
            if dx == -1 and dy == 0:
                print("north")
                now = copy.deepcopy(now_graph)
                kx, ky = 1, 0
                for i in range(n):
                    for j in range(n):
                        # print(j, i)
                        if now[j][i] > 0:
                            num = find_next_num(now, j, i, kx, ky)
                            if num == now[j][i]:
                                now[j][i] += num
                            elif num > 0:
                                now[j + kx][i + ky] += num

                        elif now[j][i] == 0:
                            num = find_next_num(now, j, i, kx, ky)
                            next_num = find_next_num(now, j, i, kx, ky)
                            if num > 0:
                                now[j][i] += num
                                if next_num == num:
                                    now[j][i] += next_num
                                elif next_num > 0:
                                    now[j + kx][i + ky] += next_num

                        # print("num", num)
                for a in range(n):
                    print(now[a])
                print()

                for a in range(n):
                    for b in range(n):
                        answer = max(answer, now[a][b])
                graphs.append(now)

            # 남
            elif dx == 1 and dy == 0:
                print("south")
                now = copy.deepcopy(now_graph)
                kx, ky = -1, 0
                for i in range(n):
                    for j in range(n - 1, -1, -1):
                        # print(j, i)
                        if now[j][i] > 0:
                            num = find_next_num(now, j, i, kx, ky)
                            if num == now[j][i]:
                                now[j][i] += num
                            elif num > 0:
                                now[j + kx][i + ky] += num

                        elif now[j][i] == 0:
                            num = find_next_num(now, j, i, kx, ky)
                            next_num = find_next_num(now, j, i, kx, ky)
                            if num > 0:
                                now[j][i] += num
                                if next_num == num:
                                    now[j][i] += next_num
                                elif next_num > 0:
                                    now[j + kx][i + ky] += next_num

                        # print("num", num)
                for a in range(n):
                    print(now[a])
                print()

                for a in range(n):
                    for b in range(n):
                        answer = max(answer, now[a][b])
                graphs.append(now)
            # 서
            elif dx == 0 and dy == -1:
                print("west")
                now = copy.deepcopy(now_graph)
                kx, ky = 0, 1
                for i in range(n):
                    for j in range(n):
                        if now[i][j] > 0:
                            num = find_next_num(now, i, j, kx, ky)
                            if num == now[i][j]:
                                now[i][j] += num
                            elif num > 0:
                                now[i + kx][j + ky] += num

                        elif now[i][j] == 0:
                            num = find_next_num(now, i, j, kx, ky)
                            next_num = find_next_num(now, i, j, kx, ky)
                            if num > 0:
                                now[i][j] += num
                                if next_num == num:
                                    now[i][j] += next_num
                                elif next_num > 0:
                                    now[i + kx][j + ky] += next_num

                        # print("num", num)
                for a in range(n):
                    print(now[a])
                print()

                for a in range(n):
                    for b in range(n):
                        answer = max(answer, now[a][b])
                graphs.append(now)

            # 동
            elif dx == 0 and dy == 1:
                print("east")
                now = copy.deepcopy(now_graph)
                kx, ky = 0, -1
                for i in range(n):
                    for j in range(n - 1, -1, -1):
                        # print(i, j)
                        if now[i][j] > 0:
                            num = find_next_num(now, i, j, kx, ky)
                            if num == now[i][j]:
                                now[i][j] += num
                            elif num > 0:
                                now[i + kx][j + ky] += num

                        elif now[i][j] == 0:
                            num = find_next_num(now, i, j, kx, ky)
                            next_num = find_next_num(now, i, j, kx, ky)
                            if num > 0:
                                now[i][j] += num
                                if next_num == num:
                                    now[i][j] += next_num
                                elif next_num > 0:
                                    now[i + kx][j + ky] += next_num

                        # print("num", num)
                for a in range(n):
                    print(now[a])
                print()

                for a in range(n):
                    for b in range(n):
                        answer = max(answer, now[a][b])
                graphs.append(now)

print("answer", answer)
print(answer)
