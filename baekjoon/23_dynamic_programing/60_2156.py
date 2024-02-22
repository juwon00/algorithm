n = int(input())
grape = [0, 0, 0]
for i in range(n):
    grape.append(int(input()))
print(grape)

dp = [0] * (n + 3)

for i in range(3, n + 3):
    print(i)
    print(dp[i - 1], dp[i - 2] + grape[i], dp[i - 3] + grape[i - 1] + grape[i])
    dp[i] = max(dp[i - 1], dp[i - 2] + grape[i], dp[i - 3] + grape[i - 1] + grape[i])
    print(dp)
print(max(dp))
