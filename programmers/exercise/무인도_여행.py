import sys

sys.setrecursionlimit(10 ** 6)


def dfs(maps, n, m, i, j, visited):
    if i < 0 or i >= n or j < 0 or j >= m or maps[i][j] == 'X' or visited[i][j]:
        return 0
    visited[i][j] = True
    total = int(maps[i][j])  # 현재 위치의 값을 누적합에 추가
    print(i, j)

    total += dfs(maps, n, m, i + 1, j, visited)
    total += dfs(maps, n, m, i - 1, j, visited)
    total += dfs(maps, n, m, i, j + 1, visited)
    total += dfs(maps, n, m, i, j - 1, visited)
    return total


def solution(maps):
    answer = []

    n = len(maps)
    m = len(maps[0])

    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        print(maps[i])

    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                sum_of_values = dfs(maps, n, m, i, j, visited)
                print(sum_of_values)
                if sum_of_values > 0:
                    answer.append(sum_of_values)

    answer.sort()
    if len(answer) == 0:
        return [-1]
    return answer


maps = ["X591X", "X1X5X", "X231X", "1XXX1"]
answer = solution(maps)
print("anwer:", answer)
