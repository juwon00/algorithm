n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
move = list(map(int, input().split()))
dice = [[0], [0, 0, 0], [0], [0]]

for g in graph:
    print(g)
print(move)
for d in dice:
    print(d)

# x 동 서 북 남
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for i in range(k):
    print(i, move[i])
    x = x + dx[move[i]]
    y = y + dy[move[i]]
    print("now", x, y)

    if x < 0 or x >= n or y < 0 or y >= m:
        print()
        x = x - dx[move[i]]
        y = y - dy[move[i]]
        continue

    if move[i] == 1:
        print("east")
        dice[1][0], dice[1][1], dice[1][2], dice[3][0] = dice[1][1], dice[1][2], dice[3][0], dice[1][0]
    elif move[i] == 2:
        print("west")
        dice[1][0], dice[1][1], dice[1][2], dice[3][0] = dice[3][0], dice[1][0], dice[1][1], dice[1][2]
    elif move[i] == 3:
        print("north")
        dice[0][0], dice[1][1], dice[2][0], dice[3][0] = dice[3][0], dice[0][0], dice[1][1], dice[2][0]
    elif move[i] == 4:
        print("south")
        dice[0][0], dice[1][1], dice[2][0], dice[3][0] = dice[1][1], dice[2][0], dice[3][0], dice[0][0]

    if graph[x][y] == 0:
        graph[x][y] = dice[1][1]

    elif graph[x][y] > 0:
        dice[1][1] = graph[x][y]
        graph[x][y] = 0

    for d in dice:
        print(d)

    print(">>>", dice[3][0])
    print()
