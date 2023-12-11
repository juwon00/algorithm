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
parent = [0] * n
for i in range(n):
    parent[i] = i

for i in range(m):
    a, b = map(int, input().split())
    print(a, b)
    if find_parent(parent, a) == find_parent(parent, b):
        print(i + 1)
        exit()
    union_parent(parent, a, b)
    print(parent)

print(0)
