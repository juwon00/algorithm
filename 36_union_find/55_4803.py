import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b:
        no_tree.append(a)
    # 처음에 생각 못한 elif 부분
    elif a in no_tree or b in no_tree:
        no_tree.append(a)
        no_tree.append(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    elif a < b:
        parent[b] = a
    else:
        parent[a] = b


cnt = 1
while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    print(n, m)
    no_tree = [0]

    parent = [i for i in range(n + 1)]
    print(parent)

    for i in range(m):
        a, b = map(int, input().split())
        print(a, b)
        union_parent(parent, a, b)
        print(parent)

    # 부모를 초기화 안하면 틀린다 왜??
    for i in range(n+1):
        parent[i] = find_parent(parent, i)
    print(parent)

    print(no_tree)
    real_tree = list(set(parent) - set(no_tree))
    print(real_tree)
    print(len(real_tree))

    if len(real_tree) == 0:
        print(f"Case {cnt}: No trees.")
    elif len(real_tree) == 1:
        print(f"Case {cnt}: There is one tree.")
    else:
        print(f"Case {cnt}: A forest of {len(real_tree)} trees.")
    cnt += 1
