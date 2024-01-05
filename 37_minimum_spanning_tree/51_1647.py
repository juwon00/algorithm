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
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()
print(edges)

result = 0
max_cost = 0
parent = [i for i in range(n + 1)]
for i in range(len(edges)):
    cost, a, b = edges[i]
    if find_parent(parent, a) != find_parent(parent, b):
        result += cost
        union_parent(parent, a, b)
        max_cost = cost

        # 기존의 코드 - max_cost를 안쓰고 이렇게 썻더니 시간오류가 생겨서 수정했다
        # if len(set(parent)) == 3:
        #     break

print(result - max_cost)
