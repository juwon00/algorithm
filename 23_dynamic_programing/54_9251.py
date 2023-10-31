# 입력 값 앞에 공백문자를 넣어서 이후에 dp 리스트 밖으로 나가지 않도록 설계
a = ' ' + input()
b = ' ' + input()

dp = [[0] * len(b) for _ in range(len(a))]
for i in range(len(dp)):
    print(dp[i])

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print()
for i in range(len(dp)):
    print(dp[i])
print(max(max(dp)))
