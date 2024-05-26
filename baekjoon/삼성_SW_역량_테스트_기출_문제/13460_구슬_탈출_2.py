from collections import deque


# x, y에서 dx, dy 방향으로 굴러갈때 최종 도착하는 위치 반환
def roll(x, y, dx, dy):
    nx, ny = x + dx, y + dy
    print(">>", nx, ny)
    if graph[nx][ny] == "." or graph[nx][ny] == "R" or graph[nx][ny] == "B":
        return roll(nx, ny, dx, dy)
    elif graph[nx][ny] == "#":
        return x, y
    elif graph[nx][ny] == "O":
        return -1, -1

# R,B가 서로 겹쳐있는 가로 혹은 세로 줄일때 True 반환 -> 이후 tx, ty를 dx, dy방향으로 한칸 뒤로 이동시키면 된다
def check(x, y, tx, ty, dx, dy):
    nx, ny = tx + dx, ty + dy
    if nx == x and ny == y:
        return True
    elif graph[nx][ny] == "." or graph[nx][ny] == "R" or graph[nx][ny] == "B":
        return check(x, y, nx, ny, dx, dy)
    elif graph[nx][ny] == "#" or graph[nx][ny] == "O":
        return False


n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(input()))

print(n, m)
for g in graph:
    print(g)

red_x, red_y = 0, 0
blue_x, blue_y = 0, 0
goal_x, goal_y = 0, 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            red_x, red_y = i, j
        elif graph[i][j] == 'B':
            blue_x, blue_y = i, j
        elif graph[i][j] == 'O':
            goal_x, goal_y = i, j
print("red", red_x, red_y, "blue", blue_x, blue_y, "goal", goal_x, goal_y)
print()

q = deque()
q.append((red_x, red_y, blue_x, blue_y, 0))

while q:
    rx, ry, bx, by, dist, = q.popleft()
    print("--------", rx, ry, bx, by, dist)
    if dist > 10:
        continue

    # 북, 남, 서, 동
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        print(dx, dy)
        print("nrx, nry start")
        nrx, nry = roll(rx, ry, dx, dy)
        print("nbx, nby start")
        nbx, nby = roll(bx, by, dx, dy)

        if nbx == -1 and nby == -1:
            print("blue -> O")
            print()
            continue
        elif nrx == -1 and nry == -1:
            if dist + 1 > 10:
                continue
            else:
                print("result", dist + 1)
                print(dist + 1)
                exit()

        if check(rx, ry, bx, by, dx, dy):
            print("b 침범")
            nbx, nby = nbx - dx, nby - dy
        elif check(bx, by, rx, ry, dx, dy):
            print("r 침범")
            nrx, nry = nrx - dx, nry - dy
        print("n", nrx, nry, nbx, nby)

        if rx != nrx or ry != nry or bx != nbx or by != nby:
            print("append")
            q.append((nrx, nry, nbx, nby, dist + 1))

        print()

print(-1)

