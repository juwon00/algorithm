# 크루스칼 알고리즘

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


def solution(n, costs):
    answer = 0

    for i in range(len(costs)):
        costs[i][0], costs[i][1], costs[i][2] = costs[i][2], costs[i][0], costs[i][1]
    costs.sort()

    parent = [0] * n
    for i in range(len(parent)):
        parent[i] = i
    print(parent)

    for i in range(len(costs)):
        print(costs[i])
        cost, a, b = costs[i]
        if find_parent(parent, a) != find_parent(parent, b):
            print("union")
            union_find(parent, a, b)
            answer += cost

    print(parent, answer)
    return answer


n = 4
costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
solution(n, costs)
