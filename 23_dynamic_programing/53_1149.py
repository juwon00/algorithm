n = int(input())
rgb = []
for i in range(n):
    rgb.append(list(map(int, input().split())))

# print(rgb)

for i in range(1, n):
    for j in range(3):
        # print(i, j)
        if j == 0:
            rgb[i][j] = min(rgb[i][j] + rgb[i - 1][j + 1], rgb[i][j] + rgb[i - 1][j + 2])
        elif j == 1:
            rgb[i][j] = min(rgb[i][j] + rgb[i - 1][j - 1], rgb[i][j] + rgb[i - 1][j + 1])
        elif j == 2:
            rgb[i][j] = min(rgb[i][j] + rgb[i - 1][j - 2], rgb[i][j] + rgb[i - 1][j - 1])

        # print(rgb)

# print()
# print(rgb)
print(min(rgb[n-1]))
