import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    print(a, b)
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    print(a, b)
    if a < b:
        parent[b] = a
        if child_fee[a] > child_fee[b]:
            child_fee[a] = child_fee[b]
        else:
            child_fee[b] = child_fee[a]
    else:
        parent[a] = b
        if child_fee[a] > child_fee[b]:
            child_fee[a] = child_fee[b]
        else:
            child_fee[b] = child_fee[a]
    print(parent)


n, m, k = map(int, input().split())

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i
print(parent)

child_fee = list(map(int, input().split()))
child_fee.insert(0, 0)

for _ in range(m):
    v, w = map(int, input().split())
    union_parent(parent, v, w)
print("parent", parent)
print(child_fee)

real_parent = set()
for i in range(len(parent)):
    fp = find_parent(parent, parent[i])
    real_parent.add(fp)
print(real_parent)

fee = 0
for i in real_parent:
    print(i)
    fee += child_fee[i]
print(fee)

if fee <= k:
    print(fee)
else:
    print("Oh no")
