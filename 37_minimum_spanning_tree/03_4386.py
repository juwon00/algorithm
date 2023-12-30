# 2차원이지만 1차원처럼 생각하면 된다

import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())

node = []
for _ in range(n):
    a, b = map(float, input().split())
    node.append((a, b))
print(node)

parent = [i for i in range(n + 1)]
edges = []
for i in range(n - 1):
    for j in range(i + 1, n):
        print("i,j", i, j)
        print(((node[i][0] - node[j][0]) ** 2 + (node[i][1] - node[j][1]) ** 2) ** (1 / 2))
        edges.append((((node[i][0] - node[j][0]) ** 2 + (node[i][1] - node[j][1]) ** 2) ** (1 / 2), i, j))
print(edges)
edges.sort()
print(edges)
print(parent)

result = 0
for i in range(len(edges)):
    cost, a, b = edges[i]
    print(cost, a, b)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(round(result, 2))
