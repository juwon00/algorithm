# 내 코드는 색상 하나하나 dfs 함수를 작성했는데
# 다른 사람들은 dfs (혹은 bfs) 를 하나만 구현해서 풀었다
# dfs 안에 지금 색상과 이후의 색상을 비교하는 코드를 넣으면 될것같다.

# 그리고 적록색맹 일때는 R을 G로 바꾼 다음 dfs 함수를 돌리면 쉽게 풀 수 있었다.

import sys
import copy

sys.setrecursionlimit(10**7)


def dfs_1_R(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if color[x][y] == 'R':
        color[x][y] = 'X'
        dfs_1_R(x - 1, y)
        dfs_1_R(x, y - 1)
        dfs_1_R(x + 1, y)
        dfs_1_R(x, y + 1)
        return True

    return False


def dfs_1_G(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if color[x][y] == 'G':
        color[x][y] = 'X'
        dfs_1_G(x - 1, y)
        dfs_1_G(x, y - 1)
        dfs_1_G(x + 1, y)
        dfs_1_G(x, y + 1)
        return True

    return False


def dfs_1_B(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if color[x][y] == 'B':
        color[x][y] = 'X'
        dfs_1_B(x - 1, y)
        dfs_1_B(x, y - 1)
        dfs_1_B(x + 1, y)
        dfs_1_B(x, y + 1)
        return True

    return False


def dfs_2_RG(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if color_2[x][y] == 'R' or color_2[x][y] == 'G':
        color_2[x][y] = 'X'
        dfs_2_RG(x - 1, y)
        dfs_2_RG(x, y - 1)
        dfs_2_RG(x + 1, y)
        dfs_2_RG(x, y + 1)
        return True

    return False


def dfs_2_B(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if color_2[x][y] == 'B':
        color_2[x][y] = 'X'
        dfs_2_B(x - 1, y)
        dfs_2_B(x, y - 1)
        dfs_2_B(x + 1, y)
        dfs_2_B(x, y + 1)
        return True

    return False


n = int(input())

color = []
for i in range(n):
    color.append(list(map(str, input())))

# for k in range(n):
#     print(color[k])

color_2 = copy.deepcopy(color)
# for k in range(n):
#     print(color_2[k])

cnt1 = 0
for i in range(n):
    for j in range(n):

        if dfs_1_R(i, j) == True:
            cnt1 += 1

        if dfs_1_G(i, j) == True:
            cnt1 += 1

        if dfs_1_B(i, j) == True:
            cnt1 += 1

cnt2 = 0
for i in range(n):
    for j in range(n):

        if dfs_2_RG(i, j) == True:
            cnt2 += 1

        if dfs_2_B(i, j) == True:
            cnt2 += 1

print(cnt1, cnt2)
