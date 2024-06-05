def check_height(x, y, slope_height):
    if road[x][y] == road[x + 1][y]:
        return True
    elif abs(road[x][y] - road[x + 1][y]) == 1:
        if road[x][y] > road[x + 1][y]:
            print("up")
            for i in range(1, l + 1):
                dx, dy = x + i, y
                if dx < 0 or dx >= n or dy < 0 or dy >= n:
                    return False
                if road[dx][dy] != road[x + 1][y]:
                    return False
                if slope_height[dx][dy] == 1:
                    return False
                slope_height[dx][dy] = 1
            return True
        else:
            print("down")
            for i in range(1, l + 1):
                dx, dy = x + 1 - i, y
                print(dx, dy)
                if dx < 0 or dx >= n or dy < 0 or dy >= n:
                    print(1)
                    return False
                if road[dx][dy] != road[x][y]:
                    print(2)
                    return False
                if slope_height[dx][dy] == 1:
                    print(3)
                    return False
                slope_height[dx][dy] = 1
            return True
    return False


def check_width(x, y, slope_width):
    if road[x][y] == road[x][y + 1]:
        return True
    elif abs(road[x][y] - road[x][y + 1]) == 1:
        if road[x][y] > road[x][y + 1]:
            print("left")
            for i in range(1, l + 1):
                dx, dy = x, y + i
                print(dx, dy)
                if dx < 0 or dx >= n or dy < 0 or dy >= n:
                    return False
                if road[dx][dy] != road[x][y + 1]:
                    return False
                if slope_width[dx][dy] == 1:
                    return False
                slope_width[dx][dy] = 1
            return True
        else:
            print("right")
            for i in range(1, l + 1):
                dx, dy = x, y + 1 - i
                print(dx, dy)
                if dx < 0 or dx >= n or dy < 0 or dy >= n:
                    print(1)
                    return False
                if road[dx][dy] != road[x][y]:
                    print(2)
                    return False
                if slope_width[dx][dy] == 1:
                    print(3)
                    return False
                slope_width[dx][dy] = 1
            return True

    return False


n, l = map(int, input().split())
road = []
for i in range(n):
    road.append(list(map(int, input().split())))
for r in road:
    print(r)

answer = 0
slope_width = [[0] * n for _ in range(n)]
slope_height = [[0] * n for _ in range(n)]

for i in range(n):
    tmp = 0
    print("------------")
    for j in range(n - 1):
        print(i, j)
        print(road[i][j])
        if check_width(i, j, slope_width):
            tmp += 1
            print("check")
        print()
    print("tmp", tmp)
    print()
    if tmp == n - 1:
        answer += 1
        print("slope ok")
        print()

print("=======")

for i in range(n):
    tmp = 0
    print("------------")
    for j in range(n - 1):
        print(j, i)
        if check_height(j, i, slope_height):
            tmp += 1
            print("check")
        print()
    if tmp == n - 1:
        answer += 1
        print("slope ok")
        print()

print(answer)
