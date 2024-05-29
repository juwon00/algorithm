from collections import deque

# 동 서 남 북
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def change_dir():
    global dir
    if mc == "L":
        if dir == (0, 1):
            dir = (-1, 0)
        elif dir == (0, -1):
            dir = (1, 0)
        elif dir == (1, 0):
            dir = (0, 1)
        elif dir == (-1, 0):
            dir = (0, -1)
    elif mc == "D":
        if dir == (0, 1):
            dir = (1, 0)
        elif dir == (0, -1):
            dir = (-1, 0)
        elif dir == (1, 0):
            dir = (0, -1)
        elif dir == (-1, 0):
            dir = (0, 1)


# 다른 사람의 접근 방식
# 다음엔 이렇게 짜도록 노력하자 !
# if time == turn[i][0]:
#         if turn[i][1] == 'L':
#             nd = (nd - 1) % 4
#         else:
#             nd = (nd + 1) % 4


def check_body(body, x, y):
    if [x, y] in body:
        return True
    else:
        return False


n = int(input())
k = int(input())

graph = [[0] * n for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 1

l = int(input())
moves = []
for _ in range(l):
    x, c = input().split()
    moves.append((int(x), c))

for m in moves:
    print(m)

move_index = 0
mx, mc = moves[move_index]

for g in graph:
    print(g)

# 동 서 남 북
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
body = deque([[0, 0]])
dir = d[0]
index = 0

while True:
    print("index", index)
    print(body)

    head_x, head_y = body[0]

    if index == mx:
        print("move!")
        change_dir()
        move_index += 1
        if move_index == len(moves):
            mx, mc = -1, -1
        else:
            mx, mc = moves[move_index]

    forward_x, forward_y = head_x + dir[0], head_y + dir[1]
    print(forward_x, forward_y)
    if forward_x < 0 or forward_y < 0 or forward_x >= n or forward_y >= n:
        print("break 1")
        break
    elif check_body(body, forward_x, forward_y):
        print("break 2")
        break

    if graph[forward_x][forward_y] == 0:
        body.appendleft([forward_x, forward_y])
        body.pop()
    elif graph[forward_x][forward_y] == 1:
        print("apple")
        graph[forward_x][forward_y] = 0  # 사과를 먹어 치워야 되는것 까지 생각하자 !
        body.appendleft([forward_x, forward_y])

    index += 1
    print(body)
    print()
    print()

print(index + 1)
