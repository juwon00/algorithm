n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
for g in graph:
    print(g)
print()
dp = [[[] for _ in range(m)] for _ in range(n)]
for i in range(m):
    dp[0][i].append((graph[0][i], 1))
    dp[0][i].append((graph[0][i], 2))
    dp[0][i].append((graph[0][i], 3))

for d in dp:
    print(d)
print()

for i in range(n):
    for j in range(m):
        print("i,j", i, j)
        for k in dp[i][j]:
            print(k)
            if i < n - 1:
                if j - 1 >= 0 and k[1] != 1:
                    dp[i + 1][j - 1].append((k[0] + graph[i + 1][j - 1], 1))
                if j + 1 <= m - 1 and k[1] != 3:
                    dp[i + 1][j + 1].append((k[0] + graph[i + 1][j + 1], 3))
                if k[1] != 2:
                    dp[i + 1][j].append((k[0] + graph[i + 1][j], 2))
        print()

for d in dp:
    print(d)
print()

result = int(1e9)
for j in range(m):
    tmp = dp[n - 1][j]
    tmp.sort()
    print(tmp)
    result = min(result, tmp[0][0])
print(result)
