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


n, m = map(int, input().split())
gender = ['X'] + list(input().split())
edges = []
for _ in range(m):
    u, v, d = map(int, input().split())
    edges.append((d, u, v))
edges.sort()

print(gender)
print(edges)

parent = [i for i in range(n + 1)]
result = 0
for i in range(len(edges)):
    cost, a, b = edges[i]
    print(cost, a, b)
    if gender[a] != gender[b] and find_parent(parent, a) != find_parent(parent, b):
        result += cost
        union_parent(parent, a, b)
        print(parent)

for i in range(n + 1):
    parent[i] = find_parent(parent, i)
print(parent)

if len(set(parent)) == 2:
    print(result)
else:
    print(-1)
