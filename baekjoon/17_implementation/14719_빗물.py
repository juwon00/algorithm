h, w = map(int, input().split())
blocks = list(map(int, input().split()))

graph = [[0] * w for _ in range(h)]

for g in graph:
    print(g)
print()
for index, b in enumerate(blocks):
    tmp = h - 1
    for _ in range(b):
        graph[tmp][index] = 1
        tmp -= 1
for g in graph:
    print(g)
print()

result = 0
for i in range(h):
    pre_block = 0
    cnt = 0
    flag = False
    for j in range(w):
        print(i, j)
        print("pre_block  ", pre_block, "\ngraph[i][j]", graph[i][j], "\nflag", flag)
        if graph[i][j] == 1 and not flag:
            print("==================start_1")
            flag = True
        # elif pre_block == 1 and graph[i][j] == 0 and not flag:
        #     print("==================start_2")
        #     flag = True
        elif graph[i][j] == 0 and flag:
            cnt += 1
            print("+1", cnt)

        elif pre_block == 0 and graph[i][j] == 1 and flag:
            print("==================finish")
            result += cnt
            cnt = 0
            flag = False
            print("==================result", result)
            if j < w - 1 and graph[i][j + 1] == 0: # 처음에 이부분 생각 못해서 조금 걸림
                print("==================start_2")
                flag = True
        pre_block = graph[i][j]
        print()

print(result)
