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

nodes = []
parent = [i for i in range(n + 1)]
for _ in range(n):
    x, y = map(int, input().split())
    nodes.append((x, y))

connected = []
for _ in range(m):
    x, y = map(int, input().split())
    connected.append((x, y))

print(parent)
print(nodes)
print(connected)

for i in range(m):
    a, b = connected[i]
    print(a, b)
    union_parent(parent, a, b)
print(parent)

edges = []
for i in range(n):
    for j in range(i + 1, n):
        print(i, j)
        length = ((nodes[i][0] - nodes[j][0]) ** 2 + (nodes[i][1] - nodes[j][1]) ** 2) ** (1 / 2)
        edges.append((length, i + 1, j + 1))
print(edges)
edges.sort()
print(edges)

result = 0
for i in range(len(edges)):
    length, a, b = edges[i]
    print(length, a, b)
    if find_parent(parent, a) != find_parent(parent, b):
        result += length
        union_parent(parent, a, b)
# print(round(result, 2))
print(format(result, ".2f"))  # 출력 부분을 신경쓸 것
