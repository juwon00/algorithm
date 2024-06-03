from collections import deque

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
for g in graph:
    print(g)

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = deque()
q.append((r, c, d))
cnt = 0
while q:
    x, y, d = q.popleft()
    print("now", x, y, d)
    if graph[x][y] == 0:
        graph[x][y] = -1
        cnt += 1

    if graph[x + dx[0]][y + dy[0]] == 0 or graph[x + dx[1]][y + dy[1]] == 0 or graph[x + dx[2]][y + dy[2]] == 0 or \
            graph[x + dx[3]][y + dy[3]] == 0:
        print("go")

        for _ in range(4):
            d -= 1
            if d == -1:
                d = 3
            print("d", d)
            if graph[x+dx[d]][y+dy[d]] == 0:
                q.append((x+dx[d], y+dy[d], d))
                break
    else:
        print("back")
        tmp = d - 2
        if tmp < 0:
            tmp += 4
        print("tmp", tmp)
        if graph[x+dx[tmp]][y+dy[tmp]] != 1:
            q.append((x+dx[tmp], y+dy[tmp], d))

    for g in graph:
        print(g)
    print()

print("cnt", cnt)
for g in graph:
    print(g)