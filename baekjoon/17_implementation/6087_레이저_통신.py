w, h = map(int, input().split())
graph = [list(input()) for _ in range(h)]

cx1, cy1, cx2, cy2 = None, None, None, None
for i in range(h):
    for j in range(w):
        if graph[i][j] == 'C' and cx1 is None:
            cx1, cy1 = i, j
            graph[i][j] = -1
            continue
        if graph[i][j] == 'C' and cx1 is not None:
            cx2, cy2 = i, j
            graph[i][j] = -2
for g in graph:
    print(g)
print(cx1, cy1, cx2, cy2)
print()

cnt = -1
while True:
    print("============================")
    print(cnt)
    for i in range(h):
        for j in range(w):
            if isinstance(graph[i][j], int) and graph[i][j] == cnt:
                print("==========")
                print(i, j, graph[i][j])

                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 상하좌우
                    print(dx, dy)
                    nx, ny = i + dx, j + dy

                    # 한 방향으로 끝까지 이동
                    while 0 <= nx < h and 0 <= ny < w:
                        if graph[nx][ny] == '*':
                            break
                        print(graph[nx][ny])
                        if graph[nx][ny] == -2:
                            print(cnt + 1)
                            exit()
                        if graph[nx][ny] == '.':
                            graph[nx][ny] = graph[i][j] + 1

                        # 다음 칸으로 이동
                        nx += dx
                        ny += dy
                for g in graph:
                    print(g)
                print()

    cnt += 1


# 다른 분의 깔끔한 풀이
# C를 찾는 부분을 배워야 겠다.
# 나는 완탐?을 돌려서 했는데 이분은 BFS로 풀었다.
# 완탐도 시간초과 안나겠다 생각해서 시작했지만 효율성을 위해 BFS로 풀면 좋을 것 같았다.
# 다익스트라로도 풀 수 있다고 한다.

# from sys import stdin
# input = stdin.readline
# from collections import deque
#
# dr = (-1, 1, 0, 0)
# dc = (0, 0, -1, 1)
#
# def bfs():
#     check = [[float('inf')] * W for _ in range(H)]
#     check[sr][sc] = -1
#     Q = deque([(sr, sc)])
#     while Q:
#         r, c = Q.popleft()
#         if (r, c) == (gr, gc):
#             return check[gr][gc]
#
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             while True:
#                 if not (0 <= nr < H and 0 <= nc < W):
#                     break
#                 if A[nr][nc] == "*":
#                     break
#                 if check[nr][nc] < check[r][c] + 1:
#                     break
#                 Q.append((nr, nc))
#                 check[nr][nc] = check[r][c] + 1
#                 nr += dr[i]
#                 nc += dc[i]
#
# # main
# W, H = map(int, input().split())
# A, C = [], []
# sr, sc, gr, gc = 0, 0, 0, 0
# for i in range(H):
#     A.append(list(input().strip()))
#     for j in range(W):
#         if A[i][j] == "C":
#             C.append((i, j))
# (sr, sc), (gr, gc) = C
# print(bfs())