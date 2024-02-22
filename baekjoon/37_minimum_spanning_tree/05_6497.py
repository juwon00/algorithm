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


while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break

    parent = [i for i in range(m)]

    edges = []
    for _ in range(n):
        x, y, z = map(int, input().split())
        edges.append((z, x, y))
    edges.sort()
    print(edges)

    result = 0
    total_cost = 0
    for i in range(len(edges)):
        cost, a, b = edges[i]
        total_cost += cost
        print(cost, a, b)
        if find_parent(parent, a) != find_parent(parent, b):
            result += cost
            union_parent(parent, a, b)
    print(parent)
    print(total_cost)
    print(result)
    print(total_cost - result)
