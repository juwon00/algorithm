n = int(input())

dp_max = [0] * 3
dp_min = [0] * 3

for i in range(n):
    graph = list(map(int, input().split()))

    print(i)
    if i == 0:
        dp_max[0], dp_max[1], dp_max[2] = graph
        dp_min[0], dp_min[1], dp_min[2] = graph
        print(dp_max)
        print(dp_min)
        continue

    max_0 = graph[0] + max(dp_max[0], dp_max[1])
    min_0 = graph[0] + min(dp_min[0], dp_min[1])

    max_1 = graph[1] + max(dp_max[0], dp_max[1], dp_max[2])
    min_1 = graph[1] + min(dp_min[0], dp_min[1], dp_min[2])

    max_2 = graph[2] + max(dp_max[1], dp_max[2])
    min_2 = graph[2] + min(dp_min[1], dp_min[2])

    dp_max[0], dp_max[1], dp_max[2] = max_0, max_1, max_2
    dp_min[0], dp_min[1], dp_min[2] = min_0, min_1, min_2
    print(dp_max)
    print(dp_min)
print()
print(dp_max)
print(dp_min)
print(max(dp_max), min(dp_min))

# 메모리 초과 나는 코드
# n = int(input())
# graph = [list(map(int, input().split())) for _ in range(n)]
# print(graph)
#
# dp_max = [[0] * 3 for _ in range(n)]
# dp_min = [[0] * 3 for _ in range(n)]
#
# for i in range(n):
#     for j in range(3):
#         if i == 0:
#             dp_max[i][j] = graph[i][j]
#             dp_min[i][j] = graph[i][j]
#             continue
#         if j == 0:
#             dp_max[i][j] = graph[i][j] + max(dp_max[i - 1][0], dp_max[i - 1][1])
#             dp_min[i][j] = graph[i][j] + min(dp_min[i - 1][0], dp_min[i - 1][1])
#         elif j == 1:
#             dp_max[i][j] = graph[i][j] + max(dp_max[i - 1][0], dp_max[i - 1][1], dp_max[i - 1][2])
#             dp_min[i][j] = graph[i][j] + min(dp_min[i - 1][0], dp_min[i - 1][1], dp_min[i - 1][2])
#         elif j == 2:
#             dp_max[i][j] = graph[i][j] + max(dp_max[i - 1][1], dp_max[i - 1][2])
#             dp_min[i][j] = graph[i][j] + min(dp_min[i - 1][1], dp_min[i - 1][2])
#
# print(dp_max)
# print(dp_min)
# print(max(dp_max[-1]), min(dp_min[-1]))
