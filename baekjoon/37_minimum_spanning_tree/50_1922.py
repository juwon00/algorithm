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
m = int(input())
edges = []
parent = [i for i in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()
print(edges)
print(parent)

result = 0
for i in range(m):
    cost, a, b = edges[i]
    if find_parent(parent, a) != find_parent(parent, b):
        result += cost
        union_parent(parent, a, b)
print(parent)
print(result)
