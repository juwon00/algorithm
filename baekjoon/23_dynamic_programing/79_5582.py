x = input()
y = input()
print("x:", x)
print("x[0]:", x[0])

x_len = len(x)
y_len = len(y)
print(len(x))
x = ' ' + x
y = ' ' + y
print(x, len(x))

dp = [[0] * (x_len + 1) for _ in range(y_len + 1)]
for d in dp:
    print(d)

result = 0
for i in range(1, y_len + 1):
    print(i)
    for j in range(1, x_len + 1):
        print(i, j)
        if x[j] == y[i]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            result = max(result, dp[i][j])

for d in dp:
    print(d)
print(result)
