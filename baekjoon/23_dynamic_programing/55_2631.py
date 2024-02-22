# 옮겨지는 아이들의 최소 횟수 -> 가장 긴 부분증가수열은 가만히 두고 나머지 아이들만 옮기면 됨

n = int(input())

kid = [0]
for _ in range(n):
    kid.append(int(input()))

dp = [1] * (n+1)

for i in range(1, n+1):
    for j in range(1, i):
        # print(i, j)
        if kid[i] > kid[j]:
            dp[i] = max(dp[i], dp[j]+1)
            # print(dp)
        # print()

# print(dp)
print(n-max(dp))

