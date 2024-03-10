def dfs(x, y):
    global result

    arr[x][y] = 'O'

    if y == c - 1:
        result += 1
        return True

    for nx, ny in [(x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]:

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue

        if arr[nx][ny] == '.':
            if dfs(nx, ny):
                return True

    return False


r, c = map(int, input().split())
arr = []
for _ in range(r):
    arr.append(list(input()))
print(r, c)

for a in arr:
    print(a)

result = 0
for i in range(r):
    dfs(i, 0)
print(result)

# 처음에는 dfs를 사용하지 않아서 틀렸다
# result = 0
# for x in range(r):
#     route = []
#     y = 0
#     print("x,y", x, y)
#
#     while True:
#
#         if y == c - 1:
#             print("find")
#             result += 1
#             for a, b in route:
#                 arr[a][b] = 'x'
#             break
#
#         print(x, y)
#
#         if 0 <= x - 1 < r and 0 <= y + 1 < c and arr[x - 1][y + 1] == ".":
#             print("up")
#             route.append((x - 1, y + 1))
#             x -= 1
#             y += 1
#         elif 0 <= x < r and 0 <= y + 1 < c and arr[x][y + 1] == ".":
#             print("right")
#             route.append((x, y + 1))
#             y += 1
#         elif 0 <= x + 1 < r and 0 <= y + 1 < c and arr[x + 1][y + 1] == ".":
#             print("bottom")
#             route.append((x + 1, y + 1))
#             x += 1
#             y += 1
#         else:
#             print("no")
#             break
#
#     for a in arr:
#         print(a)
#
#     print(x, y)
#     print()
#
# print(result)
