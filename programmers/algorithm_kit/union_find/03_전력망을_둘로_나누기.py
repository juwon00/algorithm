from collections import Counter


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


def solution(n, wires):
    answer = n

    for i in range(n - 1):

        parent = [0] * n
        for p in range(n):
            parent[p] = p
        print(parent)

        for j in range(n - 1):

            if j == i:
                continue
            print(i, j)

            print(wires[j])
            a, b = wires[j]
            if find_parent(parent, a - 1) != find_parent(parent, b - 1):
                print("union")
                union_find(parent, a - 1, b - 1)

        for k in range(len(parent)):
            parent[k] = find_parent(parent, k)

        print(parent)
        cnt = list(Counter(parent).values())

        answer = min(answer, abs(cnt[0] - cnt[1]))
        print(answer)
        print()
    print(answer)

    return answer


n = 7
wires = [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]
solution(n, wires)
