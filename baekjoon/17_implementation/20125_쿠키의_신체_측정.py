n = int(input())
graph = [list(input()) for _ in range(n)]
for g in graph:
    print(g)
heart_x, heart_y = -1, -1
for i in range(n):
    for j in range(n):
        if graph[i][j] == "*" and graph[i - 1][j] == "*" and graph[i][j - 1] == "*" and graph[i + 1][j] == "*" and \
                graph[i][j + 1] == "*":
            heart_x, heart_y = i, j
            break
    if heart_x != -1 and heart_y != -1:
        break

print(heart_x, heart_y)

left_arm = 0
for i in range(heart_y - 1, -1, -1):
    if graph[heart_x][i] == "*":
        left_arm += 1
print(left_arm)

right_arm = 0
for i in range(heart_y + 1, n):
    if graph[heart_x][i] == "*":
        right_arm += 1
print(right_arm)

waist = 0
for i in range(heart_x + 1, n):
    if graph[i][heart_y] == "*":
        waist += 1
print(waist)

left_leg = 0
for i in range(heart_x + waist + 1, n):
    if graph[i][heart_y - 1] == "*":
        left_leg += 1
print(left_leg)

right_leg = 0
for i in range(heart_x + waist + 1, n):
    if graph[i][heart_y + 1] == "*":
        right_leg += 1
print(right_leg)

print(heart_x + 1, heart_y + 1)
print(left_arm, right_arm, waist, left_leg, right_leg)
