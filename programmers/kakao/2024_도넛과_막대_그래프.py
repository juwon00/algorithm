from collections import deque


def check(i, graph):
    q = deque()
    q.append((i, 0))
    while q:
        now, dist = q.popleft()
        print(now)
        if len(graph[now]) == 2:
            return "8"
        if dist > 0 and now == i:
            return "donut"

        for j in graph[now]:
            q.append((j, dist + 1))

    return "rod"


def solution(edges):
    answer = []

    n = 0
    nums = set()
    for edge in edges:
        n = max(n, edge[0], edge[1])
        nums.add(edge[1])
    print(n)
    print(nums)

    choice = []
    for i in range(1, n + 1):
        if i not in nums:
            choice.append(i)
    print(choice)

    graph = [[] for _ in range(n + 1)]
    for edge in edges:
        graph[edge[0]].append(edge[1])
    print(graph)

    start = 0
    start_size = 0
    for c in choice:
        if start_size < len(graph[c]):
            start = c
            start_size = len(graph[c])
    print(start)
    answer.append(start)
    answer.append(0)
    answer.append(0)
    answer.append(0)

    print()
    for i in graph[start]:
        print("i", i)
        graph_shape = check(i, graph)
        print(graph_shape)
        if graph_shape == "donut":
            answer[1] += 1
        elif graph_shape == "rod":
            answer[2] += 1
        elif graph_shape == "8":
            answer[3] += 1

    return answer


edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3],
         [11, 9], [3, 8]]
answer = solution(edges)
print("answer:", answer)
