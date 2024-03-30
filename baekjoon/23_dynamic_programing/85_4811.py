# # 다시 풀어볼 문제
import math


#
# dp = [[0] * 31 for _ in range(31)]
# for j in range(31):
#     dp[0][j] = 1
#
# for i in range(1, 31):
#     for j in range(30):
#         if j == 0:
#             dp[i][j] = dp[i - 1][j + 1]
#         else:
#             dp[i][j] = dp[i][j - 1] + dp[i - 1][j + 1]
#
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     print(dp[n][0])


def catalan(n):
    return math.factorial(2 * n) // (math.factorial(n) * math.factorial(n + 1))


cat = [0] * 31
for i in range(1, 31):
    cat[i] = catalan(i)
print(cat)
while True:
    n = int(input())
    if n == 0:
        break
    print(cat[n])
