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


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    print(n, m)

    parent = [i for i in range(n + 1)]
    print(parent)

    count = 0
    for i in range(m):
        a, b = map(int, input().split())
        print(a, b)
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            count += 1
        print(parent)
    print("count", count)
    print()
