# '틀렸습니다'로 나오는데 어지서 틀린지 모르겠다. 게시판에 반례들도 다 맞는거 같은데..
# 일단은 올려놓고 다음에 수정할 예정

from collections import deque

r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
n = int(input())
heights = list(map(int, input().split()))

for g in graph:
    print(g)
print(heights)


def is_down(x, y):
    visit_list = []
    q = deque()
    visited = [[False] * c for _ in range(r)]
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        visit_list.append((x, y))

        if x == r - 1:
            visit_list = []
            return visit_list

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == 'x' and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True

    return visit_list


for index, height in enumerate(heights):
    print(height)
    height = r - height
    boom_x, boom_y = -1, -1
    if index % 2 == 0:
        print("left")
        for i in range(c):
            print(graph[height][i])
            if graph[height][i] == 'x':
                boom_x, boom_y = height, i
                break
    else:
        print("right")
        for i in range(c - 1, -1, -1):
            print(graph[height][i])
            if graph[height][i] == 'x':
                boom_x, boom_y = height, i
                break

    if boom_x == -1 and boom_y == -1:
        print("pass")
        print()
        continue
    print(boom_x, boom_y)
    graph[boom_x][boom_y] = "."

    for g in graph:
        print(g)

    down_lists = []
    for dx, dy in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
        nx, ny = boom_x + dx, boom_y + dy
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == 'x':
            print("go", nx, ny)
            down_lists.append(is_down(nx, ny))

    for down_list in down_lists:
        if down_list:
            down_cnt = r
            print(down_list)
            for down_x, down_y in down_list:
                print(down_x, down_y)
                tmp = 0
                for i in range(down_x + 1, r):
                    tmp += 1
                    print(graph[i][down_y], tmp)
                    if graph[i][down_y] == 'x' and (i, down_y) not in down_list:
                        tmp -= 1
                        down_cnt = min(down_cnt, tmp)
                        break
                down_cnt = min(down_cnt, tmp)
                print()
            print("down_cnt", down_cnt)

            down_list.sort(key=lambda x: (-x[1], -x[0]))
            print(down_list)
            for down_x, down_y in down_list:
                graph[down_x + down_cnt][down_y] = "x"
                graph[down_x][down_y] = '.'

            for g in graph:
                print(g)

    print()

for g in graph:
    print("".join(g))
