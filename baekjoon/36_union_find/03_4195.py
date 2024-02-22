import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b, count):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a != b:
        parent[b] = a
        count[a] += count[b]

    # 아래와 같이 하면 출력 초과 왜??
    # if a < b:
    #     parent[b] = a
    #     count_dict[b] = count_dict[a] + count_dict[b]
    #     count_dict[a] = count_dict[b]
    #     print(count_dict[a])
    # else:
    #     parent[a] = b
    #     count_dict[a] = count_dict[b] + count_dict[a]
    #     count_dict[b] = count_dict[a]
    #     print(count_dict[b])


t = int(input())

for _ in range(t):
    f = int(input())
    parent = dict()
    count = dict()

    for _ in range(f):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            count[a] = 1
        if b not in parent:
            parent[b] = b
            count[b] = 1
        union_parent(parent, a, b, count)
        print(count[find_parent(parent, a)])
