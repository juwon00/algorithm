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

parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i

li = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    li.append(tmp)

for a in range(n):
    for b in range(n):
        if li[a][b] == 1:
            union_parent(parent, a + 1, b + 1)

trip_city = list(map(int, input().split()))

result = []
for t in trip_city:
    tp = find_parent(parent, t)
    result.append(tp)
result_set = set(result)

if len(result_set) == 1:
    print("YES")
else:
    print("NO")
