import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
move = [list(map(int, input().split())) for _ in range(m)]
for g in graph:
    print(g)
print(move)

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
groom = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]
print(groom)
print()

for i in range(len(move)):
    print(">>>>", move[i])
    for g in graph:
        print(g)

    visited = [[False] * n for _ in range(n)]

    for j in range(len(groom)):
        print(groom[j])
        groom[j][0], groom[j][1] = (groom[j][0] + dx[move[i][0]] * move[i][1]) % n, (
                groom[j][1] + dy[move[i][0]] * move[i][1]) % n
        graph[groom[j][0]][groom[j][1]] += 1
        visited[groom[j][0]][groom[j][1]] = True

    for j in range(len(groom)):
        print(groom[j])
        cnt = 0
        for x, y in [(-1, -1), (-1, 1), (1, 1), (1, -1)]:
            tx, ty = groom[j][0] + x, groom[j][1] + y
            print(tx, ty)
            if 0 <= tx < n and 0 <= ty < n and graph[tx][ty] > 0:
                cnt += 1
        print("cnt", cnt)
        graph[groom[j][0]][groom[j][1]] += cnt
    for g in graph:
        print(g)

    tmp = []
    for x in range(n):
        for y in range(n):
            if visited[x][y] or graph[x][y] < 2:
                continue
            tmp.append([x, y])
            graph[x][y] -= 2
    groom = tmp
    print()

answer = 0
for i in range(n):
    answer += sum(graph[i])
print(answer)
