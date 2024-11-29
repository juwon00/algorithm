n, m, l, k = map(int, input().split())
stars = [list(map(int, input().split())) for _ in range(k)]
print(stars)
result = 0
for ax, ay in stars:
    for bx, by in stars:
        sx, sy = min(ax, bx), min(ay, by)
        cnt = 0
        for x, y in stars:
            if sx <= x <= sx + l and sy <= y <= sy + l:
                cnt += 1
            result = max(cnt, result)
print(k - result)

# 처음에 생각한 아이디어
# 별똥별이 떨어지는 각 점을 각각 정사각형의 왼쪽 위 / 왼쪽 아래 / 오른쪽 위 / 오른쪽 아래 꼭짓점으로 하는 경우들을 고려해보면 어떨까?
# 반례: (2, 6), (6, 2), (10, 6), (6, 10)
# result = 0
# for star_x, star_y in stars:
#     print("star_x, star_y:", star_x, star_y)
#     for i, (dx, dy) in enumerate([(-1, -1), (-1, 1), (1, 1), (1, -1)]):
#         square_x, square_y = star_x + dx * l, star_y + dy * l
#         if square_x <= 0:
#             square_x = 1
#         if square_y <= 0:
#             square_y = 1
#         if square_x > n:
#             square_x = n
#         if square_y > m:
#             square_y = m
#         if i == 0:
#             x1, y1, x2, y2 = square_x, square_y, star_x, star_y
#         elif i == 1:
#             x1, y1, x2, y2 = square_x, star_y, star_x, square_y
#         elif i == 2:
#             x1, y1, x2, y2 = star_x, star_y, square_x, square_y
#         elif i == 3:
#             x1, y1, x2, y2 = star_x, square_y, square_x, star_y
#         print("square_x, square_y:", square_x, square_y, i)
#         cnt = 0
#         for x, y in stars:
#             print(x, y)
#             if x1 <= x <= x2 and y1 <= y <= y2:
#                 cnt += 1
#             print("cnt", cnt)
#         result = max(cnt, result)
#         print()
#
#     print("=============")
#     print()
# print(k - result)
# 반례 예제
# 50 50 4 7
# 1 6
# 2 1
# 3 3
# 10 7
# 12 6
# 13 9
# 14 8
