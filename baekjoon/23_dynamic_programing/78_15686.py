import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)

for i in range(1, n + 1):
    t, p = map(int, input().split())
    dp[i] = max(dp[i], dp[i - 1])
    if i + t <= n + 1:
        print(i, i + t)
        dp[i + t - 1] = max(dp[i + t - 1], dp[i - 1] + p)
    print(dp)
print(dp[-1])

# 처음 생각한 하향식 풀이
# 39번째줄이 없어서 계속 틀렸었다.
import sys

input = sys.stdin.readline

n = int(input())
t = []
p = []
for _ in range(n):
    ti, pi = map(int, input().split())
    t.append(ti)
    p.append(pi)

print(t)
print(p)
dp = [0] * (n + 1)
print(dp)

for i in range(n - 1, -1, -1):
    print(i, i + t[i] - 1)
    if i + t[i] - 1 >= n:
        dp[i] = dp[i + 1]
        print("pass")
        continue

    dp[i] = max(dp[i + 1], dp[i + t[i]] + p[i])
    print(dp)

print(max(dp))
