n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
dp = [1] * n
graph.sort()
print(graph)
print(dp)

for i in range(1, n):
    for j in range(i):
        print()
        print(i, j)
        print(graph[i], graph[j])
        if graph[i][1] > graph[j][1]:
            print("find")
            dp[i] = max(dp[i], dp[j] + 1)
            print(dp)

print(n - max(dp))
