n = int(input())
Ti = [0]
Pi = [0]
for _ in range(n):
    t, p = map(int, input().split())
    Ti.append(t)
    Pi.append(p)
print(Ti)
print(Pi)

dp = [0] * (n + 2)

for i in range(n, 0, -1):
    print(i)
    if Ti[i] + i > n + 1:
        dp[i] = dp[i + 1]  # 이 부분 생각하기
        continue
    print(i)
    dp[i] = max(dp[i + 1], dp[i + Ti[i]] + Pi[i])
    print(dp)
print(dp[1])
