def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_find(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, computers):
    parent = [0] * n
    for p in range(len(parent)):
        parent[p] = p

    for c in computers:
        print(c)

    for i in range(len(computers)):
        for j in range(i, len(computers)):
            print(i, j)
            if i != j and computers[i][j] == 1:
                print("union")
                union_find(parent, i, j)

    print(parent)
    print(len(set(parent)))

    for i in range(len(parent)):
        parent[i] = find_parent(parent, i)

    return len(set(parent))


n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
solution(n, computers)
