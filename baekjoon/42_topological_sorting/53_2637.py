# 다시 dp부분을 생각해보면 좋을 문제

from collections import deque
import sys

input = sys.stdin.readline


def topological_sort():
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        print("now", now)

        for next, next_need in graph[now]:
            # 기본 부품
            if needs[now].count(0) == n + 1:
                needs[next][now] += next_need

            # 중간 부품
            else:
                for j in range(1, n + 1):
                    needs[next][j] += needs[now][j] * next_need

            indegree[next] -= 1

            if indegree[next] == 0:
                q.append(next)

            for nn in needs:
                print(nn)
            print(indegree)
            print()


n = int(input())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
needs = [[0] * (n + 1) for _ in range(n + 1)]

m = int(input())
for _ in range(m):
    x, y, k = map(int, input().split())
    print(x, y, k)
    graph[y].append((x, k))
    indegree[x] += 1

print(graph)
print(indegree)
print(needs)

basic = []
for i in range(1, n + 1):
    if indegree[i] == 0:
        basic.append(i)
print(basic)

topological_sort()

print(basic)

for b in basic:
    print(b, needs[n][b])
