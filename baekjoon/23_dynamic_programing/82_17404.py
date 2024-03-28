import sys

input = sys.stdin.readline

INF = int(1e9)
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
for a in arr:
    print(a)
dp1 = [[INF] * 3 for _ in range(n)]
dp2 = [[INF] * 3 for _ in range(n)]
dp3 = [[INF] * 3 for _ in range(n)]
dp1[0][0] = arr[0][0]
dp2[0][1] = arr[0][1]
dp3[0][2] = arr[0][2]

print()
for d in dp1:
    print(d)
print()
for d in dp2:
    print(d)
print()
for d in dp3:
    print(d)

for i in range(1, n):
    print(i)
    for j in range(3):
        print(i, j)
        if j == 0:
            dp1[i][j] = arr[i][j] + min(dp1[i - 1][j + 1], dp1[i - 1][j + 2])
            dp2[i][j] = arr[i][j] + min(dp2[i - 1][j + 1], dp2[i - 1][j + 2])
            dp3[i][j] = arr[i][j] + min(dp3[i - 1][j + 1], dp3[i - 1][j + 2])
        elif j == 1:
            dp1[i][j] = arr[i][j] + min(dp1[i - 1][j - 1], dp1[i - 1][j + 1])
            dp2[i][j] = arr[i][j] + min(dp2[i - 1][j - 1], dp2[i - 1][j + 1])
            dp3[i][j] = arr[i][j] + min(dp3[i - 1][j - 1], dp3[i - 1][j + 1])
        elif j == 2:
            dp1[i][j] = arr[i][j] + min(dp1[i - 1][j - 1], dp1[i - 1][j - 2])
            dp2[i][j] = arr[i][j] + min(dp2[i - 1][j - 1], dp2[i - 1][j - 2])
            dp3[i][j] = arr[i][j] + min(dp3[i - 1][j - 1], dp3[i - 1][j - 2])

dp1[-1][0] = INF
dp2[-1][1] = INF
dp3[-1][2] = INF

print()
for d in dp1:
    print(d)
print()
for d in dp2:
    print(d)
print()
for d in dp3:
    print(d)

print(min(min(dp1[-1]), min(dp2[-1]), min(dp3[-1])))
