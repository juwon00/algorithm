# 다시 풀어볼 문제

# def change(gear, rotate):
#     if rotate == 1:
#         gear = gear[-1:] + gear[:-1]
#     elif rotate == -1:
#         gear = gear[1:] + gear[:1]
#     return gear
#
#
# gears = [[]] + [list(map(int, input())) for _ in range(4)]
# k = int(input())
# moves = [tuple(map(int, input().split())) for _ in range(k)]
#
# print(gears)
# for g in gears:
#     print(g)
# print(moves)
# print()
#
# for i in range(k):
#     print(gears)
#     cur, rotate = moves[i]
#     print(cur, rotate)
#     if cur == 1:
#         if gears[1][2] != gears[2][6]:
#             if gears[2][2] != gears[3][6]:
#                 if gears[3][2] != gears[4][6]:
#                     gears[1] = change(gears[1], rotate)
#                     gears[2] = change(gears[2], -rotate)
#                     gears[3] = change(gears[3], rotate)
#                     gears[4] = change(gears[4], -rotate)
#                 else:
#                     gears[1] = change(gears[1], rotate)
#                     gears[2] = change(gears[2], -rotate)
#                     gears[3] = change(gears[3], rotate)
#             else:
#                 gears[1] = change(gears[1], rotate)
#                 gears[2] = change(gears[2], -rotate)
#
#     elif cur == 2:
#         if gears[1][2] != gears[2][6] and gears[2][2] != gears[3][6]:
#             if gears[3][2] != gears[4][6]:
#                 gears[1] = change(gears[1], -rotate)
#                 gears[2] = change(gears[2], rotate)
#                 gears[3] = change(gears[3], -rotate)
#                 gears[4] = change(gears[4], rotate)
#             else:
#                 gears[1] = change(gears[1], -rotate)
#                 gears[2] = change(gears[2], rotate)
#                 gears[3] = change(gears[3], -rotate)
#         elif gears[2][2] != gears[3][6]:
#             if gears[3][2] != gears[4][6]:
#                 gears[2] = change(gears[2], rotate)
#                 gears[3] = change(gears[3], -rotate)
#                 gears[4] = change(gears[4], rotate)
#             else:
#                 gears[2] = change(gears[2], rotate)
#                 gears[3] = change(gears[3], -rotate)
#         elif gears[1][2] != gears[2][6]:
#             gears[1] = change(gears[1], -rotate)
#             gears[2] = change(gears[2], rotate)
#
#     elif cur == 3:
#         if gears[2][2] != gears[3][6] and gears[3][2] != gears[4][6]:
#             if gears[1][2] != gears[2][6]:
#                 gears[1] = change(gears[1], rotate)
#                 gears[2] = change(gears[2], -rotate)
#                 gears[3] = change(gears[3], rotate)
#                 gears[4] = change(gears[4], -rotate)
#             else:
#                 gears[1] = change(gears[1], rotate)
#                 gears[2] = change(gears[2], -rotate)
#                 gears[3] = change(gears[3], rotate)
#         elif gears[2][2] != gears[3][6]:
#             if gears[1][2] != gears[2][6]:
#                 gears[1] = change(gears[1], rotate)
#                 gears[2] = change(gears[2], -rotate)
#                 gears[3] = change(gears[3], rotate)
#             else:
#                 gears[2] = change(gears[2], -rotate)
#                 gears[3] = change(gears[3], rotate)
#         elif gears[3][2] != gears[4][6]:
#             gears[3] = change(gears[3], rotate)
#             gears[4] = change(gears[4], -rotate)
#
#     elif cur == 4:
#         if gears[4][6] != gears[3][2]:
#             if gears[3][6] != gears[2][2]:
#                 if gears[2][6] != gears[1][2]:
#                     gears[1] = change(gears[1], -rotate)
#                     gears[2] = change(gears[2], rotate)
#                     gears[3] = change(gears[3], -rotate)
#                     gears[4] = change(gears[4], rotate)
#                 else:
#                     gears[2] = change(gears[2], rotate)
#                     gears[3] = change(gears[3], -rotate)
#                     gears[4] = change(gears[4], rotate)
#             else:
#                 gears[3] = change(gears[3], -rotate)
#                 gears[4] = change(gears[4], rotate)
#
#     print()
#
# print(gears)
# answer = 0
# if gears[1][0] == 1:
#     answer += 1
# if gears[2][0] == 1:
#     answer += 2
# if gears[3][0] == 1:
#     answer += 4
# if gears[4][0] == 1:
#     answer += 8
# print(answer)


# s = 1, n = 0


def rotation(n, d):
    if d == -1:  # 반시계 방향으로 회전
        tmp_gear = gears[n][0]
        for i in range(7): gears[n][i] = gears[n][i + 1]
        gears[n][7] = tmp_gear

    if d == 1:  # 시계 방향으로 회전
        tmp_gear = gears[n][7]
        for i in range(7, 0, -1): gears[n][i] = gears[n][i - 1]
        gears[n][0] = tmp_gear

    return


def solution(n, d):
    rs = [(n, d)]

    rdir = -d
    for i in range(n, 0, -1):
        if gears[i][6] != gears[i - 1][2]:
            rs.append((i - 1, rdir))
            rdir = -rdir
            continue
        break

    rdir = -d
    for i in range(n, 3):
        if gears[i][2] != gears[i + 1][6]:
            rs.append((i + 1, rdir))
            rdir = -rdir
            continue
        break

    for x, y in rs:
        rotation(x, y)


gears = [[int(x) for x in input()] for _ in range(4)]
K = int(input())  # 회전 횟수
info = [tuple(map(int, input().split())) for _ in range(K)]

for n, d in info: solution(n - 1, d)

answer = 0
for i in range(4):
    if gears[i][0] == 1:
        answer += 2 ** i

print(answer)
