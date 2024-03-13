n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
print(arr)

dp = [0] * (k + 1)
dp[0] = 1

print(dp)

for x in arr:
    print(x)
    for y in range(x, k + 1):
        print(x, y)
        dp[y] += dp[y - x]
    print(dp)
print(dp[k])
