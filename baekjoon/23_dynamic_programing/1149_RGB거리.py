n = int(input())
for i in range(n):
    print()
    print(i)
    rgb = list(map(int, input().split()))
    print(rgb)
    if i == 0:
        r, g, b = rgb
    elif 0 < i < n:
        r, g, b = rgb[0] + min(g, b), rgb[1] + min(r, b), rgb[2] + min(r, g)
    print(r, g, b)

print(min(r, g, b))
