for t in range(int(input())):
    graph = list(map(int, input().split()))
    n = graph.pop(0)

    # print("n", n)
    lst = [graph[i:i + n] for i in range(0, len(graph), n)]
    for i in range(n):
        for j in range(n):
            if lst[i][j] == 0:
                lst[i][j] = int(1e9)
    # for l in lst:
    #     print(l)
    # print()

    for k in range(n):
        for i in range(n):
            for j in range(n):
                lst[i][j] = min(lst[i][j], lst[i][k] + lst[k][j])

    # for l in lst:
    #     print(l)

    result = int(1e9)
    for i in range(n):
        tmp = sum(lst[i]) - lst[i][i]
        result = min(result, tmp)
    print(f"#{t + 1} {result}")
