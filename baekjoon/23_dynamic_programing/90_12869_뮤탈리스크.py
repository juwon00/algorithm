# 다시 풀어볼 문제

n = int(input())
scv = list(map(int, input().split()))
scv.extend([0, 0])
dp = [[[0] * 61 for _ in range(61)] for _ in range(61)]
dp[scv[0]][scv[1]][scv[2]] = 1

comb = [(9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 9, 3), (1, 3, 9)]
for i in range(60, -1, -1):
    for j in range(60, -1, -1):
        for k in range(60, -1, -1):
            if dp[i][j][k] > 0:
                for c in comb:
                    ni = i - c[0] if i - c[0] >= 0 else 0
                    nj = j - c[1] if j - c[1] >= 0 else 0
                    nk = k - c[2] if k - c[2] >= 0 else 0
                    if dp[ni][nj][nk] == 0 or dp[ni][nj][nk] > dp[i][j][k] + 1:
                        dp[ni][nj][nk] = dp[i][j][k] + 1

print(dp[0][0][0] - 1)
