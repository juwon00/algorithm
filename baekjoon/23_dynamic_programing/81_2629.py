wn = int(input())
weight = list(map(int, input().split()))
mn = int(input())
marble = list(map(int, input().split()))

length = max(max(marble), sum(weight)) + 1
print(length)

dp = [[0] * length for _ in range(wn + 1)]
for d in dp:
    print(d)

for i in range(1, wn + 1):
    print(i)
    dp[i][weight[i - 1]] = 1

    for j in range(1, length):
        print(i - 1, j)
        if dp[i - 1][j] == 1:
            print("find")
            if weight[i - 1] - j >= 0:
                dp[i][weight[i - 1] - j] = 1
            if j - weight[i - 1] >= 0:
                dp[i][j - weight[i - 1]] = 1
            if weight[i - 1] + j < length:
                dp[i][weight[i - 1] + j] = 1
    for k in range(length):
        if dp[i - 1][k] == 1:
            dp[i][k] = 1

    for d in dp:
        print(d)

for m in marble:
    if dp[-1][m] == 1:
        print("Y", end=" ")
    else:
        print("N", end=" ")

# 처음에 생각 못했던 반례
# 3
# 20 35 50
# 1
# 5
#
# 23, 24번째 줄을 추가해서 해결
