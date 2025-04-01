n = int(input())
score = list(map(int, input().split()))
dp = [0] * (n + 1)
print(score)
print(dp)

for i in range(1, n + 1):
    for j in range(i, 0, -1):
        print(i, j)
        print(score[j - 1:i], max(score[j - 1:i]) - min(score[j - 1:i]))
        dp[i] = max(dp[i], dp[j - 1] + max(score[j - 1:i]) - min(score[j - 1:i]))
        print(dp)
        print()

print(dp[n])
