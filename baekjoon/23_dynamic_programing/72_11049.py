# 다시 풀어 볼 문제

n = int(input())
mat = [tuple(map(int, input().split())) for i in range(n)]
print(mat)

dp = [[0] * n for i in range(n)]
for cnt in range(n - 1):
    print("cnt", cnt)
    for i in range(n - 1 - cnt):
        j = i + cnt + 1
        dp[i][j] = 2 ** 31
        print("i, j", i, j)

        for k in range(i, j):
            print(k)
            print(dp[i][k], dp[k + 1][j], mat[i][0] * mat[k][1] * mat[j][1])
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + mat[i][0] * mat[k][1] * mat[j][1])
        for d in dp:
            print(d)

    print()
    for d in dp:
        print(d)
    print()
print(dp[0][-1])
