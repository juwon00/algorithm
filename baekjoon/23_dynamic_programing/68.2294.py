n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

dp = [10001] * (k + 1)
dp[0] = 0
print(dp)

for num in arr:
    print(num)
    for i in range(num, k + 1):
        print(num, i)
        dp[i] = min(dp[i], dp[i - num] + 1)

print(dp)
print(dp[k])
if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])
