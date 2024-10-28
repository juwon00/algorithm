# 다시 풀어볼 문제
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(cur):
    visited[cur] = True
    for node in graph[cur]:
        if not visited[node]:
            dfs(node)
            print(cur, node)
            dp[cur][0] += max(dp[node])  # 현재 마을을 우수마을로 선정 X
            print(dp)
            dp[cur][1] += dp[node][0]  # 현재 마을을 우수마을로 선정
            print(dp)
            print()


n = int(input())
people = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0, people[i]] for i in range(n + 1)]  # dp[i][0] = i마을을 선정X, dp[i][1] = i마을을 선정O
visited = [False] * (n + 1)
print(graph)
print(dp)
print(visited)
print()

dfs(1)
print(dp)
print(max(dp[1]))