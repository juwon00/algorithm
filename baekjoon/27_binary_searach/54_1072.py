x, y = map(int, input().split())
z = (y * 100) // x

if z >= 99:
    print(-1)
    exit()

left = 0
right = x
result = 0

while left <= right:
    mid = (left + right) // 2

    if ((y+mid) * 100) // (x+mid) <= z:
        left = mid + 1
    else:
        result = mid
        right = mid - 1

print(result)
