import sys

input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    arr = [0] + list(map(int, input().split()))
    print(arr)

    dp = [[0] * (k + 1) for _ in range(k + 1)]

    for x in range(1, k + 1):
        for y in range(1, k + 1):
            if y == x + 1:
                print(x, y)
                dp[x][y] = arr[x] + arr[y]

    print()
    for d in dp:
        print(d)
    print()
    for i in range(k - 1, 0, -1):
        for j in range(1, k + 1):
            # print(i, j)
            if dp[i][j] == 0 and j > i:
                print(i, j)
                dp[i][j] = min(dp[i][s] + dp[s + 1][j] for s in range(i, j)) + sum(arr[i:j + 1])

    print()
    for d in dp:
        print(d)

    print(dp[1][k])
