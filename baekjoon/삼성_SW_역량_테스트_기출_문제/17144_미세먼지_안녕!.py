import sys

input = sys.stdin.readline

R, C, T = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(map(int, input().split())))

air_up, air_down = 0, 0
for r in range(R):
    if graph[r][0] == -1:
        air_up, air_down = r, r + 1
        break
if air_up == 0 and air_down == 0:
    print("false")

while T:
    diffusion = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if graph[i][j] >= 5:
                cnt = 0
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != -1:
                        diffusion[nx][ny] += graph[i][j] // 5
                        cnt += 1
                graph[i][j] = graph[i][j] - graph[i][j] // 5 * cnt

    for x in range(R):
        for y in range(C):
            graph[x][y] += diffusion[x][y]

    for a in range(air_up - 1, 0, -1):
        graph[a][0] = graph[a - 1][0]
    for b in range(0, C - 1):
        graph[0][b] = graph[0][b + 1]
    for c in range(0, air_up):
        graph[c][C - 1] = graph[c + 1][C - 1]
    for d in range(C - 1, 0, -1):
        if d == 1:
            graph[air_up][d] = 0
            continue
        graph[air_up][d] = graph[air_up][d - 1]

    for a in range(air_down + 1, R - 1):
        graph[a][0] = graph[a + 1][0]
    for b in range(0, C - 1):
        graph[R - 1][b] = graph[R - 1][b + 1]
    for c in range(R - 1, air_down - 1, -1):
        graph[c][C - 1] = graph[c - 1][C - 1]
    for d in range(C - 1, 0, -1):
        if d == 1:
            graph[air_down][d] = 0
            continue
        graph[air_down][d] = graph[air_down][d - 1]

    T = T - 1

result = 0
for r in range(R):
    result += sum(graph[r])
print(result + 2)
