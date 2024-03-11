n = int(input())

arr = [[0] * 12 for _ in range(n + 1)]

for j in range(2, 11):
    arr[1][j] = 1
for a in arr:
    print(a)

for x in range(2, n + 1):
    print(x)
    for y in range(1, 11):
        print(x, y)
        arr[x][y] = arr[x - 1][y - 1] + arr[x - 1][y + 1]

for a in arr:
    print(a)

print()
print(sum(arr[n]) % 1000000000)
