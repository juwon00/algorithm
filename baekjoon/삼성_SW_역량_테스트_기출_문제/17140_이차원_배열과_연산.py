from collections import defaultdict


def cal_r(n, m):
    print("R")
    tmp_dicts = []
    for i in range(n):
        dic = defaultdict(int)
        for j in range(m):
            if graph[i][j] != 0:
                dic[graph[i][j]] += 1
        dic = sorted(dic.items(), key=lambda x: (x[1], x[0]))
        tmp_dicts.append(dic)

    result = []
    max_len = 0
    for i in range(len(tmp_dicts)):
        tmp = []
        for j in range(len(tmp_dicts[i])):
            tmp.append(tmp_dicts[i][j][0])
            tmp.append(tmp_dicts[i][j][1])
        result.append(tmp)
        max_len = max(max_len, len(tmp))
    print(result, max_len)

    for i in range(len(result)):
        if len(result[i]) < max_len:
            more = [0] * (max_len - len(result[i]))
            result[i] = result[i] + more
    print(result)
    return result


def cal_c(n, m):
    print("C")
    tmp_dicts = []
    for i in range(m):
        dic = defaultdict(int)
        for j in range(n):
            if graph[j][i] != 0:
                dic[graph[j][i]] += 1
        dic = sorted(dic.items(), key=lambda x: (x[1], x[0]))
        tmp_dicts.append(dic)
    print(tmp_dicts)

    num_rows = len(tmp_dicts)
    flattened_2d_list = [[value for pair in sublist for value in pair] for sublist in tmp_dicts]
    num_cols = max(len(l) for l in flattened_2d_list)
    print(num_rows, num_cols)

    result = [[0] * num_rows for _ in range(num_cols)]

    for i in range(len(tmp_dicts)):
        for j in range(len(tmp_dicts[i])):
            # print(i, j, tmp_dicts[i][j][0], tmp_dicts[i][j][1])
            # print(j * 2, i)
            # print(j * 2 + 1, i)
            result[j * 2][i] = tmp_dicts[i][j][0]
            result[j * 2 + 1][i] = tmp_dicts[i][j][1]

    return result


r, c, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(3)]

for i in range(101):
    print(">>>", i)
    for g in graph:
        print(g)

    n = len(graph)
    m = len(graph[0])
    print("n,m", n, m)
    print(r - 1, c - 1)
    # print(graph[r - 1][c - 1])
    if 0 <= r - 1 < n and 0 <= c - 1 < m and graph[r - 1][c - 1] == k:
        print(i)
        exit()

    if n >= m:  # R연산
        graph = cal_r(n, m)
    elif n < m:  # C연산
        # graph = cal_c(n, m)
        graph = list(map(list, zip(*graph)))  # zip 함수를 사용해서 cal_r 구현만으로도 가능
        graph = cal_r(m, n)
        graph = list(map(list, zip(*graph)))
    print()

print(-1)
