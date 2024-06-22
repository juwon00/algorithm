n = int(input())
open1, open2 = map(int, input().split())
length = int(input())
order = [int(input()) for _ in range(length)]
print(n)
print(open1, open2)
print(length)
print(order)
INF = int(1e12)
dp = [[[INF] * (n + 1) for _ in range(n + 1)] for _ in range(length + 1)]
dp[0][open1][open2] = 1
for dd in dp:
    for d in dd:
        print(d)
    print()

for l in range(length):
    print(">>>>>>", l)
    print("order", order[l])

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dp[l][i][j] != INF:
                print("-", i, j)
                dp[l + 1][i][order[l]] = min(dp[l + 1][i][order[l]], dp[l][i][j] + abs(order[l] - j))
                dp[l + 1][order[l]][j] = min(dp[l + 1][order[l]][j], dp[l][i][j] + abs(order[l] - i))
    print()

for dd in dp:
    for d in dd:
        print(d)
    print()

answer = INF
for i in range(n + 1):
    for j in range(n + 1):
        answer = min(answer, dp[length][i][j])
print(answer - 1)
